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

from tigerline.models import Zipcode


def zipcode_import(path):
    if path:
        zipcode_mapping = {
            'code': 'ZCTA5CE10',
            'mpoly': 'POLYGON',
        }
        zipcode_shp = os.path.join(path, 'tl_2010_us_zcta510.shp')
        lm = LayerMapping(Zipcode, zipcode_shp, zipcode_mapping)
        lm.save(verbose=True)


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--path', default='', dest='path',
            help='The directory where the zipcode data is stored.'),
    )
    help = 'Installs the 2010 tigerline files for zipcodes'

    def handle(self, *args, **kwargs):
        path = kwargs['path']

        # With DEBUG on this will DIE.
        settings.DEBUG = False

        print("Zipcode Start: %s" % datetime.datetime.now())
        zipcode_import(path=os.path.join(path, 'tl_2010_us_zcta510'))
        print("End Zipcode: %s" % datetime.datetime.now())
