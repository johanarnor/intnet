from south.db import db
from south.v2 import SchemaMigration


class Migration(SchemaMigration):

    def forwards(self, orm):
        # Renaming model 'Tag' to 'RemarkTag'
        db.rename_table('activities_activityimage', 'activities_carouselimage')

    def backwards(self, orm):
        # Renaming model 'Tag' to 'RemarkTag'
        db.rename_table('activities_carouselimage', 'activities_activityimage')