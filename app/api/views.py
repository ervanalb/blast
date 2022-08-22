import itertools

from astropy.coordinates import SkyCoord
from host.models import Transient
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView

from . import datamodel
from .components import data_model_components


def transient_exists(transient_name: str) -> bool:
    """
    Checks if a transient exists in the database.

    Parameters:
        transient_name (str): transient_name.
    Returns:
        exisit (bool): True if the transient exists false otherwise.
    """
    try:
        Transient.objects.get(name__exact=transient_name)
        exists = True
    except Transient.DoesNotExist:
        exists = False
    return exists


def ra_dec_valid(ra: str, dec: str) -> bool:
    """
    Checks if a given ra and dec coordinate is valid

    Parameters:
        ra (str): Right
    """
    try:
        ra, dec = float(ra), float(dec)
        coord = SkyCoord(ra=ra, dec=dec, unit="deg")
        valid = True
    except:
        valid = False
    return valid


@api_view(["GET"])
def get_transient_science_payload(request, transient_name):
    if not transient_exists(transient_name):
        return Response(
            {"message": f"{transient_name} not in database"},
            status=status.HTTP_404_NOT_FOUND,
        )

    component_groups = [
        component_group(transient_name) for component_group in data_model_components
    ]
    components = datamodel.unpack_component_groups(component_groups)
    data = datamodel.serialize_blast_science_data(components)
    return Response(data, status=status.HTTP_200_OK)


@api_view(["POST"])
def post_transient(request, transient_name, transient_ra, transient_dec):
    if transient_exists(transient_name):
        return Response(
            {"message": f"{transient_name} already in database"},
            status=status.HTTP_409_CONFLICT,
        )

    if not ra_dec_valid(transient_ra, transient_dec):
        return Response(
            {"message": f"bad ra and dec: ra={transient_ra}, dec={transient_dec}"},
            status.HTTP_400_BAD_REQUEST,
        )

    data_string = (
        f"{transient_name}: ra = {float(transient_ra)}, dec= {float(transient_dec)}"
    )
    Transient.create(name=transient_name, ra_deg=float(transient_ra), dec_deg=float(transient_dec))
    return Response(
        {"message": f"transient successfully posted: {data_string}"},
        status=status.HTTP_201_CREATED,
    )
