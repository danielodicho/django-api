from django.db import models
from rest_framework import serializers

# Create your models here.
# class School_class(models.Model):
#     class_name = models.CharField(max_length=100)
#

class Student(models.Model):  # model for registering a new student, parameters: username and login
    # status
    user_name = models.CharField(max_length=100)
    todo_backlog = models.CharField(max_length=1000, null=True, blank=True)
    # todo_todo =
    # todo_doing =
    # todo_done =
    is_logged_in = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name


class Todo(models.Model):  # 'to do widget, parameters:title, description. Boolean: completed status, creator of widget
    title = models.CharField('title of todo', max_length=120)
    description = models.TextField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title


class download_link(models.Model):
    download_name = models.CharField(max_length=200)
    download_url = models.URLField(max_length=200)

    def __str__(self):
        return self.download_name
