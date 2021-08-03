from django.db import models


# Create your models here.
# class School_class(models.Model):
#     class_name = models.CharField(max_length=100)
#
class Student(models.Model):
    user_name = models.CharField(max_length=100)
    is_logged_in = models.BooleanField(default=False)

    def __str__(self):
        return self.user_name

    # def has_mult_todos(self):
    #     return self.todo_set.count() > 1

class Todo(models.Model):
    title = models.CharField(max_length=120)
    description = models.TextField(blank=True)
    completed = models.BooleanField(default=False)
    owner = models.ForeignKey(Student, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.title

class download_link(models.Model):
    download_name = models.CharField(max_length=200)
    download_url = models.URLField(max_length=200)

    def __str__(self):
        return self.download_name