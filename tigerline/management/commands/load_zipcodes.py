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


def zipcode_import(zipcode_shp):
    zipcode_mapping = {
        'code': 'ZCTA5CE10',
        'mpoly': 'POLYGON',
    }

    lm = LayerMapping(Zipcode, zipcode_shp, zipcode_mapping)
    lm.save(verbose=True)


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--path', default='', dest='path',
            help='The directory where the zipcode data is stored.'),
    )
    help = 'Installs the 2010/2012/2013 tigerline files for zipcodes'

    def handle(self, *args, **kwargs):
        path = kwargs['path']

        # With DEBUG on this will DIE.
        settings.DEBUG = False

        # figure out which path we want to use.
        if os.path.exists(os.path.join(path, 'tl_2013_us_zcta510')):
            print('Found 2013 files.')
            path = os.path.join(path, 'tl_2013_us_zcta510/tl_2013_us_zcta510.shp')
        elif os.path.exists(os.path.join(path, 'tl_2012_us_zcta510')):
            print('Found 2012 files.')
            path = os.path.join(path, 'tl_2012_us_zcta510/tl_2012_us_zcta510.shp')
        elif os.path.exists(os.path.join(path, 'tl_2010_us_zcta510')):
            print('Found 2010 files.')
            path = os.path.join(path, 'tl_2010_us_zcta510/tl_2010_us_zcta510.shp')
        else:
            print('Could not find files.')
            exit()

        print("Zipcode Start: %s" % datetime.datetime.now())
        zipcode_import(path)
        print("End Zipcode: %s" % datetime.datetime.now())
