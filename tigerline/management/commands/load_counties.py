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


def county_import(path):
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
    county_shp = os.path.join(path, 'tl_2010_us_county10.shp')
    lm = LayerMapping(County, county_shp, county_mapping, encoding='LATIN1')
    lm.save(verbose=True)


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--path', default='', dest='path',
            help='The directory where the county data is stored.'),
    )
    help = 'Installs the 2010 tigerline files for counties'

    def handle(self, *args, **kwargs):
        path = kwargs['path']

        # With DEBUG on this will DIE.
        settings.DEBUG = False

        print("Start Counties: %s" % datetime.datetime.now())
        county_import(path=os.path.join(path, 'tl_2010_us_county10'))
        print("End Counties: %s" % datetime.datetime.now())
