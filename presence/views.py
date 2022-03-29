from django.shortcuts import render
from  .serialize import ClassesTestSerialize
from  .models import ClassesTest
from  rest_framework import viewsets
# Create your views here.

class ClassesTestViewSet(viewsets.ModelViewSet):
    serializer_class = ClassesTestSerialize
    queryset = ClassesTest.objects.all()