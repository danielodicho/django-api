from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer, StudentSerializer,DownloadSerializer, SchoolSerializer, PkTestSerializer, PkrelationSerializer
from .models import Todo, Student, download_link, School_Class, Pk_test, Pk_relation


# Create your views here

def todo_detail(request):  # just for debug, make sure to delete this properly
    user_id = Student.objects.get(user_name = 'daniel')
    change_link = Student.objects.all()
    for x in change_link:
        y = x.user_name
        Student
    obj = Todo.objects.filter(owner=user_id.id)
    context = {
        'object': obj
    }
    return render(request, 'todo1/detail.html', context)


class PkView(viewsets.ModelViewSet):
    serializer_class = PkTestSerializer
    queryset = Pk_test.objects.all()

class RelationView(viewsets.ModelViewSet):
    serializer_class = PkrelationSerializer
    queryset = Pk_relation.objects.all()

class SchoolView(viewsets.ModelViewSet):
    serializer_class = SchoolSerializer
    queryset = School_Class.objects.all()

class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
class DownloadView(viewsets.ModelViewSet):
    serializer_class = DownloadSerializer
    queryset = download_link.objects.all()

