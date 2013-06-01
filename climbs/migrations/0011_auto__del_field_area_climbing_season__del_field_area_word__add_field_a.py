# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Deleting field 'Area.climbing_season'
        db.delete_column('climbs_area', 'climbing_season')

        # Deleting field 'Area.word'
        db.delete_column('climbs_area', 'word')

        # Adding field 'Area.winter'
        db.add_column('climbs_area', 'winter',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)


    def backwards(self, orm):
        # Adding field 'Area.climbing_season'
        db.add_column('climbs_area', 'climbing_season',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=500, blank=True),
                      keep_default=False)

        # Adding field 'Area.word'
        db.add_column('climbs_area', 'word',
                      self.gf('django.db.models.fields.BooleanField')(default=False),
                      keep_default=False)

        # Deleting field 'Area.winter'
        db.delete_column('climbs_area', 'winter')


    models = {
        'climbs.area': {
            'Meta': {'object_name': 'Area'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'approach_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'approach_difficulty': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'approach_distance': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'approach_time': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'area_parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['climbs.Area']", 'null': 'True', 'blank': 'True'}),
            'area_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'bouldering': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'fall': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'garage_parking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hazard_information': ('django.db.models.fields.CharField', [], {'max_length': '750', 'blank': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'lot_parking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'misc_information': ('django.db.models.fields.CharField', [], {'max_length': '750', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nearest_emergency': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'nearest_emergency_address': ('django.db.models.fields.CharField', [], {'max_length': '150', 'blank': 'True'}),
            'nearest_emergency_phone': ('django.contrib.localflavor.us.models.PhoneNumberField', [], {'max_length': '20', 'null': 'True', 'blank': 'True'}),
            'parking_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'parking_latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'parking_longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'pet_friendly': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'pullout_parking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rock_type': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'sport': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'spring': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'street_parking': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'summer': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'top_rope': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trad': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trailhead_latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'trailhead_longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'weather_description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'winter': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'zipcode': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'})
        },
        'climbs.areaphoto': {
            'Meta': {'object_name': 'AreaPhoto'},
            'area': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['climbs.Area']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_type': ('django.db.models.fields.CharField', [], {'max_length': '1'})
        },
        'climbs.problem': {
            'Meta': {'object_name': 'Problem'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'angle': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'aspect': ('django.db.models.fields.CharField', [], {'max_length': '50', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'features': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'first_ascent': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'grade': ('django.db.models.fields.CharField', [], {'max_length': '6'}),
            'hazard_information': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'height': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'landing_information': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'location': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'misc_information': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['climbs.Area']"}),
            'problem_descent': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'problem_start': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'quality': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'max_length': '50'}),
            'source': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'}),
            'variations': ('django.db.models.fields.CharField', [], {'max_length': '100', 'blank': 'True'})
        },
        'climbs.problemphoto': {
            'Meta': {'object_name': 'ProblemPhoto'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'problem': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['climbs.Problem']"})
        }
    }

    complete_apps = ['climbs']