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
        ))
        db.send_create_signal('climbs', ['Route'])

        # Adding model 'Photo'
        db.create_table('climbs_photo', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('photo', self.gf('django.db.models.fields.files.ImageField')(max_length=100)),
            ('photo_type', self.gf('django.db.models.fields.CharField')(max_length=1)),
            ('route', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['climbs.Route'])),
            ('quality_rating', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('climbs', ['Photo'])


    def backwards(self, orm):
        # Deleting model 'Route'
        db.delete_table('climbs_route')

        # Deleting model 'Photo'
        db.delete_table('climbs_photo')


    models = {
        'climbs.photo': {
            'Meta': {'object_name': 'Photo'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'photo': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'photo_type': ('django.db.models.fields.CharField', [], {'max_length': '1'}),
            'quality_rating': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['climbs.Route']"})
        },
        'climbs.route': {
            'Meta': {'object_name': 'Route'},
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'difficulty': ('django.db.models.fields.CharField', [], {'max_length': '15'}),
            'height': ('django.db.models.fields.IntegerField', [], {'null': 'True'}),
            'history': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'quality_rating': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50'}),
            'weather': ('django.db.models.fields.TextField', [], {'blank': 'True'})
        }
    }

    complete_apps = ['climbs']