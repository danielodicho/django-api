from django.contrib import admin
from .models import Todo, Student, download_link, School_Class


# Register your models here.
class SchoolAdmin(admin.ModelAdmin):
    list_display = ('class_name', 'id')

class StudentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'is_logged_in', 'backlog', 'to_do', 'doing', 'done')

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'owner', 'id')
class DownloadLinksAdmin(admin.ModelAdmin):
    list_display = ('download_name', 'download_url')

admin.site.register(Student, StudentAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(download_link, DownloadLinksAdmin)
admin.site.register(School_Class, SchoolAdmin)