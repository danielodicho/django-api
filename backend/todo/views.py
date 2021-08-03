from django.shortcuts import render
from rest_framework import viewsets
from .serializers import TodoSerializer, StudentSerializer,DownloadSerializer
from .models import Todo, Student, download_link


# Create your views here

def todo_detail(request):  # just for debug, make sure to delete this properly
    obj = Todo.objects.get(id=1)
    context = {
        'object': obj
    }
    return render(request, 'todo1/detail.html', context)

class StudentView(viewsets.ModelViewSet):
    serializer_class = StudentSerializer
    queryset = Student.objects.all()

class TodoView(viewsets.ModelViewSet):
    serializer_class = TodoSerializer
    queryset = Todo.objects.all()
class DownloadView(viewsets.ModelViewSet):
    serializer_class = DownloadSerializer
    queryset = download_link.objects.all()