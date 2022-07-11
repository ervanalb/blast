import pandas as pd
from django.conf import settings
from django.test import TestCase
from numpy.testing import assert_array_equal
from sedpy.observate import Filter as SedpyFilter

from ..models import Filter
from ..prospector import filter_to_sedpy_filter


class FilterTest(TestCase):
    fixtures = [
        "../fixtures/initial/setup_survey_data.yaml",
        "../fixtures/initial/setup_filter_data.yaml",
    ]

    def test_filter_conversion(self):
        """
        Test blast filter is converted to sedpy filter
        """

        for filter in Filter.objects.all():
            # raw_data = pd.read_csv(f'{settings.TRANSMISSION_CURVES_ROOT}/{filter.name}.txt',
            #                  header=None, delim_whitespace=True)
            # raw_wavelength, raw_transmission = raw_data[0].values, raw_data[1].values
            sedpy_filter = filter_to_sedpy_filter(filter)
            self.assertTrue(sedpy_filter.nick == filter.name)
            self.assertTrue(isinstance(sedpy_filter, SedpyFilter))
            # assert_array_equal(sedpy_filter.wavelength, raw_wavelength)
            # assert_array_equal(sedpy_filter.transmission, raw_transmission)


# class PropsectorBuildObsTest(TestCase):
#    fixtures = []

##    def test_build_obs(self):
#       pass
