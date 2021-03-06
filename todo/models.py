from django.db import models
from django.contrib.postgres.fields import ArrayField

# Create your models here.
class School_Class(models.Model):
    class_name = models.CharField(max_length=100)

    def __str__(self):
        return self.class_name
#

class Student(models.Model):  # model for registering a new student, parameters: username and login
    # status
    user_name = models.CharField(max_length=100)
    backlog = ArrayField(models.CharField(max_length=1000), blank=True, null=True)
    to_do = ArrayField(models.CharField(max_length=1000), blank=True, null=True)
    doing =ArrayField(models.CharField(max_length=1000), blank=True, null=True)
    done = ArrayField(models.CharField(max_length=1000), blank=True, null=True)

    xp = models.IntegerField( default=0)
    cash = models.IntegerField(default=0)
    # todo_todo =
    # todo_doing =
    # todo_done =
    is_logged_in = models.BooleanField(default=False)
    class_name = models.ForeignKey(School_Class, on_delete=models.CASCADE, null=True)

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
    checkpoint = models.IntegerField(default=0)
    download_name = models.CharField(max_length=200)
    download_url = models.URLField(max_length=200)
    video_url = models.URLField(max_length=200, blank=True)
    challenges = ArrayField(models.CharField(max_length=1000), blank=True, null=True)
    def __str__(self):
        return self.download_name
