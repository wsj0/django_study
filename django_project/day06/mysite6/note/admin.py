from django.contrib import admin
from . import models
# Register your models here.
#note/admin.py
class NoteManager(admin.ModelAdmin):
    list_display = ['id','title','user']

admin.site.register(models.Note,NoteManager)
