from django.contrib import admin
from .models import Task
from django.urls import path

# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display = ('task', 'is_completed', 'created_at', 'update_at')
    search_fields = ('task',)
    
admin.site.register(Task,TaskAdmin)