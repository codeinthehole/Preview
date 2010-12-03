# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'PageVersion.page'
        db.add_column('main_pageversion', 'page', self.gf('django.db.models.fields.related.ForeignKey')(default=None, to=orm['main.Page']), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'PageVersion.page'
        db.delete_column('main_pageversion', 'page_id')


    models = {
        'main.client': {
            'Meta': {'object_name': 'Client'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        },
        'main.page': {
            'Meta': {'object_name': 'Page'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'project': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Project']"})
        },
        'main.pageversion': {
            'Meta': {'object_name': 'PageVersion'},
            'approval_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True'}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'image': ('django.db.models.fields.files.ImageField', [], {'max_length': '100'}),
            'number': ('django.db.models.fields.IntegerField', [], {'default': '1'}),
            'page': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Page']"}),
            'status': ('django.db.models.fields.CharField', [], {'default': "'Open'", 'max_length': '32'})
        },
        'main.project': {
            'Meta': {'object_name': 'Project'},
            'client': ('django.db.models.fields.related.ForeignKey', [], {'to': "orm['main.Client']"}),
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'description': ('django.db.models.fields.TextField', [], {'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'})
        }
    }

    complete_apps = ['main']
