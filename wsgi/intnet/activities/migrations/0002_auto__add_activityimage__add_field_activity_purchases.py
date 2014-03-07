# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'ActivityImage'
        db.create_table(u'activities_activityimage', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('title', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('image', self.gf('django.db.models.fields.files.FileField')(max_length=100)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['activities.Activity'])),
        ))
        db.send_create_signal(u'activities', ['ActivityImage'])

        # Adding field 'Activity.purchases'
        db.add_column(u'activities_activity', 'purchases',
                      self.gf('django.db.models.fields.IntegerField')(default=0),
                      keep_default=False)


    def backwards(self, orm):
        # Deleting model 'ActivityImage'
        db.delete_table(u'activities_activityimage')

        # Deleting field 'Activity.purchases'
        db.delete_column(u'activities_activity', 'purchases')


    models = {
        u'activities.activity': {
            'Meta': {'object_name': 'Activity'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['activities.Price']"}),
            'purchases': ('django.db.models.fields.IntegerField', [], {'default': '0'})
        },
        u'activities.activityimage': {
            'Meta': {'object_name': 'ActivityImage'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['activities.Activity']"}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.FileField', [], {'max_length': '100'}),
            'title': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'activities.feature': {
            'Meta': {'object_name': 'Feature'},
            'activity': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['activities.Activity']"}),
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'feature': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'})
        },
        u'activities.featureoption': {
            'Meta': {'object_name': 'FeatureOption'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'feature': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['activities.Feature']"}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'option': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        u'activities.price': {
            'Meta': {'object_name': 'Price'},
            'adult': ('django.db.models.fields.IntegerField', [], {}),
            'child': ('django.db.models.fields.IntegerField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'senior': ('django.db.models.fields.IntegerField', [], {}),
            'student': ('django.db.models.fields.IntegerField', [], {}),
            'youth': ('django.db.models.fields.IntegerField', [], {})
        }
    }

    complete_apps = ['activities']