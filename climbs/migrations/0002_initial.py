# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Route'
        db.create_table('climbs_route', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('difficulty', self.gf('django.db.models.fields.CharField')(max_length=15)),
            ('description', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('quality_rating', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
            ('height', self.gf('django.db.models.fields.IntegerField')(null=True)),
            ('weather', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('history', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['climbs.Area'])),
        ))
        db.send_create_signal('climbs', ['Route'])

        # Adding model 'RoutePhoto'
        db.create_table('climbs_routephoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('photo_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('route', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['climbs.Route'])),
            ('quality_rating', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('climbs', ['RoutePhoto'])

        # Adding model 'Area'
        db.create_table('climbs_area', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('name', self.gf('django.db.models.fields.CharField')(max_length=100)),
            ('slug', self.gf('django.db.models.fields.SlugField')(unique=True, max_length=50)),
            ('about', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('parking_desc', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('parking_gps', self.gf('django.db.models.fields.DecimalField')(null=True, max_digits=9, decimal_places=6)),
            ('approach_desc', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('approach_rating', self.gf('django.db.models.fields.CharField')(max_length=15, blank=True)),
            ('approach_length', self.gf('django.db.models.fields.TextField')(blank=True)),
            ('misc', self.gf('django.db.models.fields.TextField')(blank=True)),
        ))
        db.send_create_signal('climbs', ['Area'])

        # Adding model 'AreaPhoto'
        db.create_table('climbs_areaphoto', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('photo_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('area', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['climbs.Area'])),
            ('quality_rating', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('climbs', ['AreaPhoto'])


    def backwards(self, orm):
        # Deleting model 'Route'
        db.delete_table('climbs_route')

        # Deleting model 'RoutePhoto'
        db.delete_table('climbs_routephoto')

        # Deleting model 'Area'
        db.delete_table('climbs_area')

        # Deleting model 'AreaPhoto'
        db.delete_table('climbs_areaphoto')


    models = {
        'climbs.area': {
            'Meta': {'object_name': 'Area'},
            'about': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'approach_desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'approach_length': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'approach_rating': ('django.db.models.fields.CharField', [], {'max_length': '15', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'misc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'parking_desc': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'parking_gps': ('django.db.models.fields.DecimalField', [], {'null': 'True', 'max_digits': '9', 'decimal_places': '6'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'})
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
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'history': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quality_rating': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
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