from django.shortcuts import render
from .serializer import StudentSerializer
from .models import Student
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
import io
# Create your views here.

@csrf_exempt
def stuget(request):
    if request.method == 'GET':
        data = request.body
        stream = io.BytesIO(data)
        python = JSONParser().parse(stream)
        id = python.get('id',None)
        if id is None:
            item = Student.objects.all()
            serialize = StudentSerializer(item,many = True)
            return JsonResponse(serialize.data,safe=False)
        else:
            item = Student.objects.get(id=id)
            serialize = StudentSerializer(item)
            return JsonResponse(serialize.data,safe=False)
    if request.method == 'PUT':
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        id = python_data.get('id',None)
        item = Student.objects.get(id=id)
        serialize = StudentSerializer(item,data=python_data,partial = True)
        if serialize.is_valid():
            serialize.save()
    if request.method == 'POST':
        data = request.body
        stream = io.BytesIO(data)
        python_data = JSONParser().parse(stream)
        serialize = StudentSerializer(data=python_data)
        if serialize.is_valid():
            serialize.save()
            
#this is comment