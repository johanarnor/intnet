# -*- coding: utf-8 -*-
from south.utils import datetime_utils as datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Adding model 'Price'
        db.create_table(u'activities_price', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('adult', self.gf('django.db.models.fields.IntegerField')()),
            ('youth', self.gf('django.db.models.fields.IntegerField')()),
            ('child', self.gf('django.db.models.fields.IntegerField')()),
            ('student', self.gf('django.db.models.fields.IntegerField')()),
            ('senior', self.gf('django.db.models.fields.IntegerField')()),
        ))
        db.send_create_signal(u'activities', ['Price'])

        # Adding model 'Activity'
        db.create_table(u'activities_activity', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('label', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('description', self.gf('django.db.models.fields.TextField')()),
            ('price', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['activities.Price'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modification_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'activities', ['Activity'])

        # Adding model 'Feature'
        db.create_table(u'activities_feature', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('feature', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('activity', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['activities.Activity'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modification_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'activities', ['Feature'])

        # Adding model 'FeatureOption'
        db.create_table(u'activities_featureoption', (
            (u'id', self.gf('django.db.models.fields.AutoField')(primary_key=True)),
            ('option', self.gf('django.db.models.fields.CharField')(max_length=255)),
            ('feature', self.gf('django.db.models.fields.related.ForeignKey')(to=orm['activities.Feature'])),
            ('creation_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
            ('modification_date', self.gf('django.db.models.fields.DateTimeField')(auto_now_add=True, blank=True)),
        ))
        db.send_create_signal(u'activities', ['FeatureOption'])


    def backwards(self, orm):
        # Deleting model 'Price'
        db.delete_table(u'activities_price')

        # Deleting model 'Activity'
        db.delete_table(u'activities_activity')

        # Deleting model 'Feature'
        db.delete_table(u'activities_feature')

        # Deleting model 'FeatureOption'
        db.delete_table(u'activities_featureoption')


    models = {
        u'activities.activity': {
            'Meta': {'object_name': 'Activity'},
            'creation_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {}),
            u'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'label': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'modification_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'price': ('django.db.models.fields.related.ForeignKey', [], {'to': u"orm['activities.Price']"})
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