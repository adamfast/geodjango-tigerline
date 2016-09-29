import datetime
import os
import sys
from optparse import make_option

from django.core.management.base import BaseCommand
from django.conf import settings

try:
    from django.contrib.gis.utils import LayerMapping
except ImportError:
    print("gdal is required")
    sys.exit(1)

from tigerline.models import County

def county_import(county_shp, year):
    if year == "2010":
        county_mapping = {
            'state_fips_code': 'STATEFP10',
            'fips_code': 'COUNTYFP10',
            'county_identifier': 'GEOID10',
            'name': 'NAME10',
            'name_and_description': 'NAMELSAD10',
            'legal_statistical_description': 'LSAD10',
            'fips_55_class_code': 'CLASSFP10',
            'feature_class_code': 'MTFCC10',
            'functional_status': 'FUNCSTAT10',
            'mpoly': 'POLYGON',
        }
    else:
        county_mapping = {
            'state_fips_code': 'STATEFP',
            'fips_code': 'COUNTYFP',
            'county_identifier': 'GEOID',
            'name': 'NAME',
            'name_and_description': 'NAMELSAD',
            'legal_statistical_description': 'LSAD',
            'fips_55_class_code': 'CLASSFP',
            'feature_class_code': 'MTFCC',
            'functional_status': 'FUNCSTAT',
            'mpoly': 'POLYGON',
        }
    lm = LayerMapping(County, county_shp, county_mapping, encoding='LATIN1')
    lm.save(verbose=True)


class Command(BaseCommand):
    help = 'Installs the 2010-2016 tigerline files for counties'

    def add_arguments(self, parser):
        parser.add_argument('--path', default='', dest='path',
            help='The directory where the county data is stored.'
        )

    def handle(self, *args, **kwargs):
        path = kwargs['path']

        # With DEBUG on this will DIE.
        settings.DEBUG = False

        # figure out which path we want to use.
        years = ["2016", "2015", "2014", "2013", "2012", "2011", "2010"]
        directories = [('tl_%s_us_county' % year, year) for year in years]

        tiger_file = ""
        for (directory, year) in directories:
            if year == "2010":
                directory = directory + "10"

            if os.path.exists(os.path.join(path, directory)):
                print('Found %s files.' % year)
                tiger_file = os.path.join(path, directory + "/" + directory + ".shp")
                break

        if not tiger_file:
            print('Could not find files.')
            exit()

        print("Start Counties: %s" % datetime.datetime.now())
        county_import(tiger_file, year)
        print("End Counties: %s" % datetime.datetime.now())
