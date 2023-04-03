from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json = request.body # data in bytes
        json_data = io.BytesIO(json) # data in json
        pythondata = JSONParser().parse(json_data) #data in python type
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            
        