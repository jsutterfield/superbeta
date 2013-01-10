# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding field 'Area.state'
        db.add_column('climbs_area', 'state',
                      self.gf('django.contrib.localflavor.us.models.USStateField')(max_length=2, null=True, blank=True),
                      keep_default=False)

        # Adding field 'Area.zipcode'
        db.add_column('climbs_area', 'zipcode',
                      self.gf('django.contrib.localflavor.us.models.USPostalCodeField')(max_length=2, null=True, blank=True),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting field 'Area.state'
        db.delete_column('climbs_area', 'state')

        # Deleting field 'Area.zipcode'
        db.delete_column('climbs_area', 'zipcode')


    models = {
        'climbs.area': {
            'Meta': {'object_name': 'Area'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'approach_desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'approach_gps_lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'approach_gps_long': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'approach_length': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'approach_rating': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'misc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parking_desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'parking_gps_lat': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'parking_gps_long': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique': 'True', 'max_length': '50', 'populate_from': "'name'", 'unique_with': '()'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'}),
            'weather': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'zipcode': ('django.contrib.localflavor.us.models.USPostalCodeField', [], {'max_length': '2', 'null': 'True', 'blank': 'True'})
        },
        'climbs.areaphoto': {
            'Meta': {'object_name': 'AreaPhoto'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['climbs.Area']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'quality_rating': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'})
        },
        'climbs.route': {
            'Meta': {'object_name': 'Route'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['climbs.Area']"}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'difficulty': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'history': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quality_rating': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': "('area__name',)", 'max_length': '50', 'populate_from': "'name'"}),
            'weather': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        },
        'climbs.routephoto': {
            'Meta': {'object_name': 'RoutePhoto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'quality_rating': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['climbs.Route']"})
        }
    }

    complete_apps = ['climbs']