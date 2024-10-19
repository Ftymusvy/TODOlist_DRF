from rest_framework import serializers
from task.models import TodoTask


class TodoTaskSerializer(serializers.ModelSerializer):
    class Meta:
         model = TodoTask
         fields= ['title' , 'created', 'category']