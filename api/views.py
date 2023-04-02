from django.shortcuts import render
from rest_framework.renderers import JSONRenderer
from .serializer import StudentSerializer
from django.http import HttpResponse
from .models import Student

# Create your views here.
def student(request):
    items = Student.objects.all()
    serializer = StudentSerializer(items,many= True)
    json = JSONRenderer().render(serializer.data)
    return HttpResponse(json,content_type='application/json')
    