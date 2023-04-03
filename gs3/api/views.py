from django.shortcuts import render
from .serializer import StudentSerializer
from .models import Student
from django.http import HttpResponse,JsonResponse
from rest_framework.parsers import JSONParser
import io
# Create your views here.


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