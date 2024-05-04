from django.contrib import admin
from .models import *

class TaskAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_created', 'time_spent', 'task']

admin.site.register(Task, TaskAdmin)

