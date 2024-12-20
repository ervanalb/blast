from django.test import TestCase

from ..models import AperturePhotometry
from ..models import Transient
from ..transient_tasks import GlobalAperturePhotometry
from ..transient_tasks import LocalAperturePhotometry
from ..transient_tasks import ValidateGlobalPhotometry
from ..transient_tasks import ValidateLocalPhotometry


class TestValidatePhotometry(TestCase):
    fixtures = [
        "../fixtures/test/test_2010H_onefilter.yaml",
    ]

    def test_validate_local_photometry(self):
        transient = Transient.objects.get(name="2010H")
        vlp_cls = ValidateLocalPhotometry(transient_name=transient.name)

        status_message = vlp_cls._run_process(transient)

        # let's see which photometry is validated and which isn't
        validated_local_aperture_photometry = AperturePhotometry.objects.filter(
            transient=transient, aperture__type="local", is_validated=True
        )
        for v in validated_local_aperture_photometry:
            assert (
                "WISE_W2" not in v.filter.name
                and "WISE_W3" not in v.filter.name
                and "WISE_W4" not in v.filter.name
            )

        assert status_message == "processed"

    def test_validate_global_photometry(self):
        transient = Transient.objects.get(name="2010H")
        vgp_cls = ValidateGlobalPhotometry(transient_name=transient.name)

        status_message = vgp_cls._run_process(transient)

        not_validated_global_aperture_photometry = AperturePhotometry.objects.filter(
            transient=transient, aperture__type="global", is_validated=False
        )

        assert len(not_validated_global_aperture_photometry) == 0

    def test_global_aperture_photometry(self):
        transient = Transient.objects.get(name="2010H")
        apphot_cls = GlobalAperturePhotometry(transient_name=transient.name)

        status_message = apphot_cls._run_process(transient)

        assert status_message == "processed"

    def test_local_aperture_redshifts(self):
        transient = Transient.objects.get(name="2010H")
        transient.redshift = None
        transient.host.redshift = None
        transient.host.photometric_redshift = None
        transient.save()
        apphot_cls = LocalAperturePhotometry(transient_name=transient.name)

        status_message = apphot_cls._run_process(transient)

        assert status_message == "failed"
