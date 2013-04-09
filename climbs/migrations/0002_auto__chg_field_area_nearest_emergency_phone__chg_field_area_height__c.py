# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):

        # Changing field 'Area.nearest_emergency_phone'
        db.alter_column('climbs_area', 'nearest_emergency_phone', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Area.height'
        db.alter_column('climbs_area', 'height', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Area.zipcode'
        db.alter_column('climbs_area', 'zipcode', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Area.approach_distance'
        db.alter_column('climbs_area', 'approach_distance', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Area.approach_time'
        db.alter_column('climbs_area', 'approach_time', self.gf('django.db.models.fields.IntegerField')(null=True))

        # Changing field 'Problem.height'
        db.alter_column('climbs_problem', 'height', self.gf('django.db.models.fields.IntegerField')(null=True))

    def backwards(self, orm):

        # Changing field 'Area.nearest_emergency_phone'
        db.alter_column('climbs_area', 'nearest_emergency_phone', self.gf('django.db.models.fields.SmallIntegerField')(null=True))

        # Changing field 'Area.height'
        db.alter_column('climbs_area', 'height', self.gf('django.db.models.fields.SmallIntegerField')(null=True))

        # Changing field 'Area.zipcode'
        db.alter_column('climbs_area', 'zipcode', self.gf('django.db.models.fields.SmallIntegerField')(null=True))

        # Changing field 'Area.approach_distance'
        db.alter_column('climbs_area', 'approach_distance', self.gf('django.db.models.fields.SmallIntegerField')(null=True))

        # Changing field 'Area.approach_time'
        db.alter_column('climbs_area', 'approach_time', self.gf('django.db.models.fields.SmallIntegerField')(null=True))

        # Changing field 'Problem.height'
        db.alter_column('climbs_problem', 'height', self.gf('django.db.models.fields.SmallIntegerField')(null=True))

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
            'climbing_season': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hazard_information': ('django.db.models.fields.CharField', [], {'max_length': '750', 'blank': 'True'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'misc_information': ('django.db.models.fields.CharField', [], {'max_length': '750', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nearest_emergency': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'nearest_emergency_address': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'nearest_emergency_phone': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
            'nearest_emergttency_two_address': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'parking_description': ('django.db.models.fields.CharField', [], {'max_length': '750', 'blank': 'True'}),
            'parking_latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'parking_longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'parking_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'pet_friendly': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'rock_type': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'short_description': ('django.db.models.fields.CharField', [], {'max_length': '120', 'blank': 'True'}),
            'slug': ('autoslug.fields.AutoSlugField', [], {'unique_with': "('state',)", 'max_length': '50', 'populate_from': "'name'"}),
            'sport': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'state': ('django.contrib.localflavor.us.models.USStateField', [], {'max_length': '2'}),
            'street_address': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'top_rope': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trad': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'trailhead_latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'trailhead_longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'weather_description': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
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
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True', 'blank': 'True'}),
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