import os
from django.conf import settings
from django.contrib.gis.utils import LayerMapping
from tigerline.models import Zipcode, State, County

def zipcode_import(path='/root/tiger-line/'):
    zipcode_mapping = {
        'code': 'ZCTA5CE00',
        'mpoly': 'MULTIPOLYGON',
    }
    zipcode_shp = os.path.join(path, 'tl_2008_us_zcta500.shp')
    lm = LayerMapping(Zipcode, zipcode_shp, zipcode_mapping)
    lm.save(verbose=True)

def state_import(path='/root/tiger-line/'):
    state_mapping = {
        'fips_code': 'STATEFP',
        'usps_code': 'STUSPS',
        'name': 'NAME',
        'area_description_code': 'LSAD',
        'feature_class_code': 'MTFCC',
        'functional_status': 'FUNCSTAT',
        'mpoly': 'MULTIPOLYGON',
    }
    state_shp = os.path.join(path, 'tl_2008_us_state.shp')
    lm = LayerMapping(State, state_shp, state_mapping)
    lm.save(verbose=True)

def county_import(path='/root/tiger-line/'):
    county_mapping = {
        'state_fips_code': 'STATEFP',
        'fips_code': 'COUNTYFP',
        'county_identifier': 'CNTYIDFP',
        'name': 'NAME',
        'name_and_description': 'NAMELSAD',
        'legal_statistical_description': 'LSAD',
        'fips_55_class_code': 'CLASSFP',
        'feature_class_code': 'MTFCC',
        'functional_status': 'FUNCSTAT',
        'mpoly': 'MULTIPOLYGON',
    }
    county_shp = os.path.join(path, 'tl_2008_us_county.shp')
    lm = LayerMapping(County, county_shp, county_mapping, encoding='LATIN1')
    lm.save(verbose=True)


if __name__ == '__main__':
    import_zipcodes = True
    import_states = True
    import_counties = True

    if settings.DEBUG:
        print('With DEBUG on this will DIE. Change it and ask again.')
    else:
        import datetime
        print("Begin: %s" % datetime.datetime.now())
        if import_zipcodes:
            print("Zipcode Start: %s" % datetime.datetime.now())
            zipcode_import(path='/home/adam/Downloads/tigerline')
            print("End Zipcode: %s" % datetime.datetime.now())
        if import_states:
            print("Start States: %s" % datetime.datetime.now())
            state_import(path='/home/adam/Downloads/tigerline')
            print("End States: %s" % datetime.datetime.now())
        if import_counties:
            print("Start Counties: %s" % datetime.datetime.now())
            county_import(path='/home/adam/Downloads/tigerline')
            print("End Counties: %s" % datetime.datetime.now())
        print("All Finished: %s" % datetime.datetime.now())
