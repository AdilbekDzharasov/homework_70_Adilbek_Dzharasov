from django.contrib import admin
from webapp.models import Task, Status, Type
from webapp.models.projects import Project


class TaskAdmin(admin.ModelAdmin):
    list_display = ['id', 'summary', 'description', 'status', 'project']
    list_filter = ['id', 'summary', 'description', 'status', 'type', 'project']
    search_fields = ['id', 'summary', 'description']
    fields = ['summary', 'description', 'status', 'type', 'project', 'created_at', 'updated_at']
    readonly_fields = ['id', 'created_at', 'updated_at']


admin.site.register(Task, TaskAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ['id', 'status_title']
    list_filter = ['id', 'status_title']
    search_fields = ['id', 'status_title']
    fields = ['status_title']
    readonly_fields = ['id']


admin.site.register(Status, StatusAdmin)


class TypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'type_title']
    list_filter = ['id', 'type_title']
    search_fields = ['id', 'type_title']
    fields = ['type_title']
    readonly_fields = ['id']


admin.site.register(Type, TypeAdmin)


class ProjectAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description', 'is_deleted', 'beginning_date', 'expiration_date']
    list_filter = ['id', 'title', 'description', 'is_deleted', 'beginning_date', 'expiration_date']
    search_fields = ['id', 'title']
    fields = ['title', 'description', 'is_deleted', 'beginning_date', 'expiration_date']
    readonly_fields = ['id', 'created_at']


admin.site.register(Project, ProjectAdmin)

