import os
from django.conf import settings
from django.contrib.gis.utils import LayerMapping
from tigerline.models import Zipcode, State, County

def zipcode_import(path='/root/tiger-line/'):
    zipcode_mapping = {
        'code': 'ZCTA5CE10',
        'mpoly': 'POLYGON',
    }
    zipcode_shp = os.path.join(path, 'tl_2010_us_zcta510.shp')
    lm = LayerMapping(Zipcode, zipcode_shp, zipcode_mapping)
    lm.save(verbose=True)

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

def county_import(path='/root/tiger-line/'):
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
            zipcode_import(path='/Users/afast/Public/tigerline-2010/tl_2010_us_zcta510')
            print("End Zipcode: %s" % datetime.datetime.now())
        if import_states:
            print("Start States: %s" % datetime.datetime.now())
            state_import(path='/Users/afast/Public/tigerline-2010/tl_2010_us_state10')
            print("End States: %s" % datetime.datetime.now())
        if import_counties:
            print("Start Counties: %s" % datetime.datetime.now())
            county_import(path='/Users/afast/Public/tigerline-2010/tl_2010_us_county10')
            print("End Counties: %s" % datetime.datetime.now())
        print("All Finished: %s" % datetime.datetime.now())
