from django.contrib import admin
from .models import Todo, Student, download_link


# Register your models here.


class StudentAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'is_logged_in', 'todo_list')

class TodoAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'completed', 'owner', 'id')
class DownloadLinksAdmin(admin.ModelAdmin):
    list_display = ('download_name', 'download_url')

admin.site.register(Student, StudentAdmin)
admin.site.register(Todo, TodoAdmin)
admin.site.register(download_link, DownloadLinksAdmin)