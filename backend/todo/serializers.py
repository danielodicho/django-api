from rest_framework import serializers
from .models import Todo, Student, download_link


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = ('user_name', 'is_logged_in')

class TodoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Todo
        fields = ('id', 'title', 'description','completed' )
class DownloadSerializer(serializers.ModelSerializer):
    class Meta:
        model = download_link
        fields = ('download_name', 'download_url')