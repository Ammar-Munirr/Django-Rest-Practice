from rest_framework import serializers
from .models import Student

class StudentSerializer(serializers.Serializer):
    name = serializers.CharField(max_length = 100)
    age = serializers.IntegerField()
    
    
    
    def update(self,instance,validated):
        instance.name = validated.get('name',instance.name)
        instance.age = validated.get('age',instance.age)
        instance.save()
        return instance
    
    
    def create(self,validated):
        return Student.objects.create(**validated)