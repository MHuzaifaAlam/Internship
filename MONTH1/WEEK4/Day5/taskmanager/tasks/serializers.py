from rest_framework import serializers
from .models import Task,Project,User
from django.contrib.auth import get_user_model

User=get_user_model()
class ProjectSerializer(serializers.ModelSerializer):




    class Meta:
        model=Project
        fields=["id","title"]

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model=User
        fields=["id","username"]



class TaskSerializer(serializers.ModelSerializer):
    project=ProjectSerializer()
    assigned_to=UserSerializer(many=True)
    def validate_title(self,value):
        if len(value)<5:
            raise serializers.ValidationError("" \
            "TITLE MUST BE AT LEAST 5 CHARACTERS LONG")
        return value

    def validate(self, data):
        estimated=data.get("estimated_hours")
        actual=data.get("actual_hours")

        if actual>estimated:
            raise serializers.ValidationError(
                "Actual hours cannot be greater then estimated hours"
            )
        return data
    def validate_estimated_hours(self,value):
        if value <= 0:
            raise serializers.ValidationError("The estimated hours can not be Zero or Less then Zero")

        
    class Meta:
        model = Task
        fields = "__all__"

