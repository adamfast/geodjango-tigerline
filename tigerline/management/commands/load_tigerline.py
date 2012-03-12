import datetime
import sys
from optparse import make_option

from django.conf import settings
from django.core.management import call_command
from django.core.management.base import BaseCommand

try:
    from django.contrib.gis.utils import LayerMapping
except ImportError:
    print("gdal is required")
    sys.exit(1)


class Command(BaseCommand):
    option_list = BaseCommand.option_list + (
        make_option('--path', default='', dest='path',
            help='The directory where the TIGER/LINE data is stored.'),
    )
    help = 'Installs the 2010 TIGER/LINE files for all zipcodes, all states, and all counties'

    def handle(self, *args, **kwargs):
        path = kwargs['path']

        # With DEBUG on this will DIE.
        settings.DEBUG = False

        print("Begin: %s" % datetime.datetime.now())

        call_command('load_zipcodes', path=path)
        call_command('load_states', path=path)
        call_command('load_counties', path=path)

        print("All Finished: %s" % datetime.datetime.now())
