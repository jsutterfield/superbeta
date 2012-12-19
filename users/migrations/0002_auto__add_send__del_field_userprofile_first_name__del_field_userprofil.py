# -*- coding: utf-8 -*-
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Send'
        db.create_table('users_send', (
            ('id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('route', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['climbs.Route'])),
            ('user', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['auth.User'])),
            ('date_sent', self.gf('django.db.models.fields.DateField')(null=True, blank=True)),
            ('send_type', self.gf('django.db.models.fields.CharField')(max_length=1, blank=True)),
        ))
        db.send_create_signal('users', ['Send'])

        # Deleting field 'UserProfile.first_name'
        db.delete_column('users_userprofile', 'first_name')

        # Deleting field 'UserProfile.last_name'
        db.delete_column('users_userprofile', 'last_name')

        # Deleting field 'UserProfile.email'
        db.delete_column('users_userprofile', 'email')

        # Adding field 'UserProfile.avatar'
        db.add_column('users_userprofile', 'avatar',
                      self.gf('django.db.models.fields.files.ImageField')(default='/static/default-avatar.png', max_length=100),
                      keep_default=False)

        # Adding M2M table for field favorites on 'UserProfile'
        db.create_table('users_userprofile_favorites', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['users.userprofile'], null=False)),
            ('route', models.ForeignKey(orm['climbs.route'], null=False))
        ))
        db.create_unique('users_userprofile_favorites', ['userprofile_id', 'route_id'])

        # Adding M2M table for field projects on 'UserProfile'
        db.create_table('users_userprofile_projects', (
            ('id', models.AutoField(verbose_name='ID', primary_key=True, auto_created=True)),
            ('userprofile', models.ForeignKey(orm['users.userprofile'], null=False)),
            ('route', models.ForeignKey(orm['climbs.route'], null=False))
        ))
        db.create_unique('users_userprofile_projects', ['userprofile_id', 'route_id'])


    def backwards(self, orm):
        # Deleting model 'Send'
        db.delete_table('users_send')

        # Adding field 'UserProfile.first_name'
        db.add_column('users_userprofile', 'first_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=20, blank=True),
                      keep_default=False)

        # Adding field 'UserProfile.last_name'
        db.add_column('users_userprofile', 'last_name',
                      self.gf('django.db.models.fields.CharField')(default='', max_length=30, blank=True),
                      keep_default=False)


        # User chose to not deal with backwards NULL issues for 'UserProfile.email'
        raise RuntimeError("Cannot reverse this migration. 'UserProfile.email' and its values cannot be restored.")
        # Deleting field 'UserProfile.avatar'
        db.delete_column('users_userprofile', 'avatar')

        # Removing M2M table for field favorites on 'UserProfile'
        db.delete_table('users_userprofile_favorites')

        # Removing M2M table for field projects on 'UserProfile'
        db.delete_table('users_userprofile_projects')


    models = {
        'auth.group': {
            'Meta': {'object_name': 'Group'},
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '80'}),
            'permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'})
        },
        'auth.permission': {
            'Meta': {'ordering': "('content_type__app_label', 'content_type__model', 'codename')", 'unique_together': "(('content_type', 'codename'),)", 'object_name': 'Permission'},
            'codename': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'content_type': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['contenttypes.ContentType']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '50'})
        },
        'auth.user': {
            'Meta': {'object_name': 'User'},
            'date_joined': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'email': ('django.db.models.fields.EmailField', [], {'max_length': '75', 'blank': 'True'}),
            'first_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'groups': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Group']", 'symmetrical': 'False', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'is_active': ('django.db.models.fields.BooleanField', [], {'default': 'True'}),
            'is_staff': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'is_superuser': ('django.db.models.fields.BooleanField', [], {'default': 'False'}),
            'last_login': ('django.db.models.fields.DateTimeField', [], {'default': 'datetime.datetime.now'}),
            'last_name': ('django.db.models.fields.CharField', [], {'max_length': '30', 'blank': 'True'}),
            'password': ('django.db.models.fields.CharField', [], {'max_length': '128'}),
            'user_permissions': ('django.db.models.fields.related.ManyToManyField', [], {'to': "orm['auth.Permission']", 'symmetrical': 'False', 'blank': 'True'}),
            'username': ('django.db.models.fields.CharField', [], {'unique': 'True', 'max_length': '30'})
        },
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
            'weather': ('django.db.models.fields.TextField', [], {'blank': 'True'})
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
        'contenttypes.contenttype': {
            'Meta': {'ordering': "('name',)", 'unique_together': "(('app_label', 'model'),)", 'object_name': 'ContentType', 'db_table': "'django_content_type'"},
            'app_label': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'model': ('django.db.models.fields.CharField', [], {'max_length': '100'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '100'})
        },
        'users.send': {
            'Meta': {'object_name': 'Send'},
            'date_sent': ('django.db.models.fields.DateField', [], {'null': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'route': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['climbs.Route']"}),
            'send_type': ('django.db.models.fields.CharField', [], {'max_length': '1', 'blank': 'True'}),
            'user': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['auth.User']"})
        },
        'users.userprofile': {
            'Meta': {'object_name': 'UserProfile'},
            'avatar': ('django.db.models.fields.files.ImageField', [], {'default': "'/static/default-avatar.png'", 'max_length': '100'}),
            'favorites': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_favorites'", 'symmetrical': 'False', 'to': "orm['climbs.Route']"}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'projects': ('django.db.models.fields.related.ManyToManyField', [], {'related_name': "'user_projects'", 'symmetrical': 'False', 'to': "orm['climbs.Route']"}),
            'user': ('django.db.models.fields.related.OneToOneField', [], {'to': "orm['auth.User']", 'unique': 'True'})
        }
    }

    complete_apps = ['users']