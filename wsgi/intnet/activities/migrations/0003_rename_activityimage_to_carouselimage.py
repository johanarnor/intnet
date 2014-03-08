from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Renaming model 'Tag' to 'RemarkTag'
        db.rename_table('activities_activityimage', 'activities_carouselimage')

    def backwards(self, orm):
        # Renaming model 'Tag' to 'RemarkTag'
        db.rename_table('activities_carouselimage', 'activities_activityimage')

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
        u'activities.carouselimage': {
            'Meta': {'object_name': 'CarouselImage'},
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