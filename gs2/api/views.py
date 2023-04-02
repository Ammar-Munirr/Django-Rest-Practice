from django.shortcuts import render
from .models import Student
from .serializer import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json = request.body
        json_data = io.BytesIO(json)
        pythondata = JSONParser().parse(json_data)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()
            
        