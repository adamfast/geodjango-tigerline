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

from tigerline.models import State


def state_import(state_shp):
    if '2014' in state_shp or '2013' in state_shp or '2012' in state_shp or '2011' in state_shp:
        state_mapping = {
            'fips_code': 'STATEFP',
            'usps_code': 'STUSPS',
            'name': 'NAME',
            'area_description_code': 'LSAD',
            'feature_class_code': 'MTFCC',
            'functional_status': 'FUNCSTAT',
            'mpoly': 'POLYGON',
        }
    else:
        state_mapping = {
            'fips_code': 'STATEFP10',
            'usps_code': 'STUSPS10',
            'name': 'NAME10',
            'area_description_code': 'LSAD10',
            'feature_class_code': 'MTFCC10',
            'functional_status': 'FUNCSTAT10',
            'mpoly': 'POLYGON',
        }
    lm = LayerMapping(State, state_shp, state_mapping)
    lm.save(verbose=True)


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--path', default='', dest='path',
            help='The directory where the state data is stored.'),
    )
    help = 'Installs the 2010 tigerline files for states'

    def handle(self, *args, **kwargs):
        path = kwargs['path']

        # With DEBUG on this will DIE.
        settings.DEBUG = False

        if os.path.exists(os.path.join(path, 'tl_2014_us_state')):
            print('Found 2014 files.')
            path = os.path.join(path, 'tl_2014_us_state/tl_2014_us_state.shp')
        elif os.path.exists(os.path.join(path, 'tl_2013_us_state')):
            print('Found 2013 files.')
            path = os.path.join(path, 'tl_2013_us_state/tl_2013_us_state.shp')
        elif os.path.exists(os.path.join(path, 'tl_2012_us_state')):
            print('Found 2012 files.')
            path = os.path.join(path, 'tl_2012_us_state/tl_2012_us_state.shp')
        elif os.path.exists(os.path.join(path, 'tl_2011_us_state')):
            print('Found 2011 files.')
            path = os.path.join(path, 'tl_2011_us_state/tl_2011_us_state.shp')
        elif os.path.exists(os.path.join(path, 'tl_2010_us_state10')):
            print('Found 2010 files.')
            path = os.path.join(path, 'tl_2010_us_state10/tl_2010_us_state10.shp')
        else:
            print('Could not find files.')
            exit()

        print("Start States: %s" % datetime.datetime.now())
        if path:
            state_import(path)
        print("End States: %s" % datetime.datetime.now())
