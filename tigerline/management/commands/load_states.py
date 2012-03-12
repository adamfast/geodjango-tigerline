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


def state_import(path='/root/tiger-line/'):
    state_mapping = {
        'fips_code': 'STATEFP10',
        'usps_code': 'STUSPS10',
        'name': 'NAME10',
        'area_description_code': 'LSAD10',
        'feature_class_code': 'MTFCC10',
        'functional_status': 'FUNCSTAT10',
        'mpoly': 'POLYGON',
    }
    state_shp = os.path.join(path, 'tl_2010_us_state10.shp')
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

        print("Start States: %s" % datetime.datetime.now())
        state_import(path=os.path.join(path, 'tl_2010_us_state10'))
        print("End States: %s" % datetime.datetime.now())
