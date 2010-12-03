# encoding: utf-8
import datetime
from south.db import db
from south.v2 import SchemaMigration
from django.db import models

class Migration(SchemaMigration):

    def forwards(self, orm):
        
        # Adding field 'Project.slug'
        db.add_column('main_project', 'slug', self.gf('django.db.models.fields.SlugField')(default='test', unique=True, max_length=50, db_index=True), keep_default=False)

        # Adding field 'Client.slug'
        db.add_column('main_client', 'slug', self.gf('django.db.models.fields.SlugField')(default='test', unique=True, max_length=50, db_index=True), keep_default=False)


    def backwards(self, orm):
        
        # Deleting field 'Project.slug'
        db.delete_column('main_project', 'slug')

        # Deleting field 'Client.slug'
        db.delete_column('main_client', 'slug')


    models = {
        'main.client': {
            'Meta': {'object_name': 'Client'},
            'created_date': ('django.db.models.fields.DateTimeField', [], {'auto_now_add': 'True', 'blank': 'True'}),
            'id': ('django.db.models.fields.AutoField', [], {'primary_key': 'True'}),
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
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
            'approval_date': ('django.db.models.fields.DateTimeField', [], {'null': 'True', 'blank': 'True'}),
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
            'name': ('django.db.models.fields.CharField', [], {'max_length': '255'}),
            'slug': ('django.db.models.fields.SlugField', [], {'unique': 'True', 'max_length': '50', 'db_index': 'True'})
        }
    }

    complete_apps = ['main']
