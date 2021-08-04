from rest_framework import serializers
from .models import Todo, Student, download_link


class StudentSerializer(serializers.ModelSerializer):  #available fields for the API
    class Meta:
        model = Student
        fields = ('id', 'user_name', 'is_logged_in')


class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('title', 'description', 'completed', 'owner')


class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = download_link
        fields = ('download_name', 'download_url')
