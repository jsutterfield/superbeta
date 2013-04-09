# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Area'
        db.create_table('climbs_area', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('area_type', self.gf('django.db.models.fields.CharField')(max_length=2)),
            ('area_parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['climbs.Area'], null=True, blank=True)),
            ('state', self.gf('django.contrib.localflavor.us.models.USStateField')(max_length=2)),
            ('city', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=6, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=6, blank=True)),
            ('street_address', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('zipcode', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('bouldering', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('top_rope', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('sport', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('trad', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('approach_difficulty', self.gf('django.db.models.fields.CharField')(max_length=12, blank=True)),
            ('approach_time', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('approach_distance', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('approach_description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('trailhead_longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=6, blank=True)),
            ('trailhead_latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=6, blank=True)),
            ('parking_type', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('parking_longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=6, blank=True)),
            ('parking_latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=6, blank=True)),
            ('parking_description', self.gf('django.db.models.fields.CharField')(max_length=750, blank=True)),
            ('height', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('about', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('rock_type', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('weather_description', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('climbing_season', self.gf('django.db.models.fields.CharField')(max_length=500, blank=True)),
            ('hazard_information', self.gf('django.db.models.fields.CharField')(max_length=750, blank=True)),
            ('misc_information', self.gf('django.db.models.fields.CharField')(max_length=750, blank=True)),
            ('pet_friendly', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('nearest_emergency', self.gf('django.db.models.fields.CharField')(max_length=25, blank=True)),
            ('nearest_emergency_address', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('nearest_emergency_phone', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('nearest_emergttency_two_address', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('slug', self.gf('autoslug.fields.AutoSlugField')(unique_with=('state',), max_length=50, populate_from='name')),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
        ))
        db.send_create_signal('climbs', ['Area'])

        # Adding model 'Problem'
        db.create_table('climbs_problem', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('parent', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['climbs.Area'])),
            ('featured', self.gf('django.db.models.fields.BooleanField')(default=False)),
            ('grade', self.gf('django.db.models.fields.CharField')(max_length=6)),
            ('quality', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('longitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=6, blank=True)),
            ('latitude', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=6, blank=True)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('height', self.gf('django.db.models.fields.SmallIntegerField')(null=True, blank=True)),
            ('angle', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('features', self.gf('django.db.models.fields.CharField')(max_length=40, blank=True)),
            ('short_description', self.gf('django.db.models.fields.CharField')(max_length=120, blank=True)),
            ('about', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('location', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('problem_start', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('problem_descent', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('landing_information', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('hazard_information', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('aspect', self.gf('django.db.models.fields.CharField')(max_length=50, blank=True)),
            ('variations', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('misc_information', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
            ('first_ascent', self.gf('django.db.models.fields.CharField')(max_length=20, blank=True)),
            ('source', self.gf('django.db.models.fields.CharField')(max_length=100, blank=True)),
        ))
        db.send_create_signal('climbs', ['Problem'])

        # Adding model 'ProblemPhoto'
        db.create_table('climbs_problemphoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('problem', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['climbs.Problem'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
        ))
        db.send_create_signal('climbs', ['ProblemPhoto'])

        # Adding model 'AreaPhoto'
        db.create_table('climbs_areaphoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['climbs.Area'])),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('photo_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
        ))
        db.send_create_signal('climbs', ['AreaPhoto'])


    def backwards(self, orm):
        # Deleting model 'Area'
        db.delete_table('climbs_area')

        # Deleting model 'Problem'
        db.delete_table('climbs_problem')

        # Deleting model 'ProblemPhoto'
        db.delete_table('climbs_problemphoto')

        # Deleting model 'AreaPhoto'
        db.delete_table('climbs_areaphoto')


    models = {
        'climbs.area': {
            'Meta': {'object_name': 'Area'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'approach_description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'approach_difficulty': ('django.db.models.fields.CharField', [], {'max_length': '12', 'blank': 'True'}),
            'approach_distance': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'approach_time': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'area_parent': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['climbs.Area']", 'null': 'True', 'blank': 'True'}),
            'area_type': ('django.db.models.fields.CharField', [], {'max_length': '2'}),
            'bouldering': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'city': ('django.db.models.fields.CharField', [], {'max_length': '20', 'blank': 'True'}),
            'climbing_season': ('django.db.models.fields.CharField', [], {'max_length': '500', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'featured': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'hazard_information': ('django.db.models.fields.CharField', [], {'max_length': '750', 'blank': 'True'}),
            'height': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'latitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'longitude': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6', 'blank': 'True'}),
            'misc_information': ('django.db.models.fields.CharField', [], {'max_length': '750', 'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'nearest_emergency': ('django.db.models.fields.CharField', [], {'max_length': '25', 'blank': 'True'}),
            'nearest_emergency_address': ('django.db.models.fields.CharField', [], {'max_length': '40', 'blank': 'True'}),
            'nearest_emergency_phone': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
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
            'zipcode': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'})
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
            'height': ('django.db.models.fields.SmallIntegerField', [], {'null': 'True', 'blank': 'True'}),
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