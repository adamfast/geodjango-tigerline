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
    help = 'Installs the 2010-2106 tigerline files for zipcodes'

    def add_arguments(self, parser):
        parser.add_argument('--path', default='', dest='path',
            help='The directory where the zipcode data is stored.'
        )

    def handle(self, *args, **kwargs):
        path = kwargs['path']

        # With DEBUG on this will DIE.
        settings.DEBUG = False

        # figure out which path we want to use.
        years = ["2016", "2015", "2014", "2013", "2012", "2010"]
        directories = [('tl_%s_us_zcta510' % year, year) for year in years]

        tiger_file = ""
        for (directory, year) in directories:
            if os.path.exists(os.path.join(path, directory)):
                print('Found %s files.' % year)
                tiger_file = os.path.join(path, directory + "/" + directory + ".shp")
                break

        if not tiger_file:
            print('Could not find files.')
            exit()

        print("Zipcode Start: %s" % datetime.datetime.now())
        zipcode_import(tiger_file)
        print("End Zipcode: %s" % datetime.datetime.now())
