# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding index on 'Zipcode', fields ['code']
        db.create_index('tigerline_zipcode', ['code'])

        # Adding index on 'State', fields ['name']
        db.create_index('tigerline_state', ['name'])


    def backwards(self, orm):
        
        # Removing index on 'State', fields ['name']
        db.delete_index('tigerline_state', ['name'])

        # Removing index on 'Zipcode', fields ['code']
        db.delete_index('tigerline_zipcode', ['code'])


    models = {
        'tigerline.county': {
            'Meta': {'object_name': 'County'},
            'county_identifier': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'feature_class_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'fips_55_class_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'fips_code': ('django.db.models.fields.CharField', [], {'max_length': '3'}),
            'functional_status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'legal_statistical_description': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'mpoly': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name_and_description': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'state_fips_code': ('django.db.models.fields.CharField', [], {'max_length': "'2'"})
        },
        'tigerline.state': {
            'Meta': {'ordering': "['name']", 'object_name': 'State'},
            'area_description_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'feature_class_code': ('django.db.models.fields.CharField', [], {'max_length': '5'}),
            'fips_code': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'functional_status': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpoly': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100', 'db_index': 'True'}),
            'usps_code': ('django.db.models.fields.CharField', [], {'max_length': '2'})
        },
        'tigerline.zipcode': {
            'Meta': {'ordering': "['code']", 'object_name': 'Zipcode'},
            'code': ('django.db.models.fields.CharField', [], {'max_length': '5', 'db_index': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'mpoly': ('django.contrib.gis.db.models.fields.MultiPolygonField', [], {})
        }
    }

    complete_apps = ['tigerline']
