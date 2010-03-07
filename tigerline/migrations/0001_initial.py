from south.db import db
from django.db import models
from tigerline.models import *

class Migration:
    def forwards(self, orm):
        # Adding model 'State'
        db.create_table('tigerline_state', (
            ('id', orm['tigerline.State:id']),
            ('fips_code', orm['tigerline.State:fips_code']),
            ('usps_code', orm['tigerline.State:usps_code']),
            ('name', orm['tigerline.State:name']),
            ('area_description_code', orm['tigerline.State:area_description_code']),
            ('feature_class_code', orm['tigerline.State:feature_class_code']),
            ('functional_status', orm['tigerline.State:functional_status']),
            ('mpoly', orm['tigerline.State:mpoly']),
        ))
        db.send_create_signal('tigerline', ['State'])

        # Adding model 'Zipcode'
        db.create_table('tigerline_zipcode', (
            ('id', orm['tigerline.Zipcode:id']),
            ('code', orm['tigerline.Zipcode:code']),
            ('mpoly', orm['tigerline.Zipcode:mpoly']),
        ))
        db.send_create_signal('tigerline', ['Zipcode'])

        # Adding model 'County'
        db.create_table('tigerline_county', (
            ('id', orm['tigerline.County:id']),
            ('state_fips_code', orm['tigerline.County:state_fips_code']),
            ('fips_code', orm['tigerline.County:fips_code']),
            ('county_identifier', orm['tigerline.County:county_identifier']),
            ('name', orm['tigerline.County:name']),
            ('name_and_description', orm['tigerline.County:name_and_description']),
            ('legal_statistical_description', orm['tigerline.County:legal_statistical_description']),
            ('fips_55_class_code', orm['tigerline.County:fips_55_class_code']),
            ('feature_class_code', orm['tigerline.County:feature_class_code']),
            ('functional_status', orm['tigerline.County:functional_status']),
            ('mpoly', orm['tigerline.County:mpoly']),
        ))
        db.send_create_signal('tigerline', ['County'])

    def backwards(self, orm):
        # Deleting model 'State'
        db.delete_table('tigerline_state')
        # Deleting model 'Zipcode'
        db.delete_table('tigerline_zipcode')
        # Deleting model 'County'
        db.delete_table('tigerline_county')

    models = {
        'tigerline.county': {
            'county_identifier': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'feature_class_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'fips_55_class_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'fips_code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'functional_status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legal_statistical_description': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'mpoly': ('models.MultiPolygonField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_and_description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state_fips_code': ('django.db.models.fields.CharField', [], {'max_length': "'2'"})
        },
        'tigerline.state': {
            'area_description_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'feature_class_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'fips_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'functional_status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpoly': ('models.MultiPolygonField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'usps_code': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'tigerline.zipcode': {
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpoly': ('models.MultiPolygonField', [], {})
        }
    }

    complete_apps = ['tigerline']
