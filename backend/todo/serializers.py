from rest_framework import serializers
from .models import Todo, Student, download_link, School_Class


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School_Class
        fields = ('class_name', 'id')

class StudentSerializer(serializers.ModelSerializer):  #available fields for the API
    class Meta:
        model = Student
        fields = ('id', 'user_name', 'is_logged_in', 'cash', 'xp', 'class_name', 'backlog', 'to_do', 'doing', 'done')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'completed', 'owner')


class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = download_link
        fields = ('download_name', 'download_url', 'checkpoint', 'video_url', 'challenges')
