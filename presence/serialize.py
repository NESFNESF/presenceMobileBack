from  rest_framework import serializers
from .models import ClassesTest

class ClassesTestSerialize(serializers.ModelSerializer):
    class Meta:
        model = ClassesTest
        fields = '__all__'