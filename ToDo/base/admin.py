from django.contrib import admin
from .models import TaskModel

# Register your models here.


class TaskModelAdmin(admin.ModelAdmin):
    list_display = (
        'id','title','priority','complete'
    )
    readonly_fields = ['id']

    def display_id(self, obj):
        return obj.id

admin.site.register(TaskModel, TaskModelAdmin)
