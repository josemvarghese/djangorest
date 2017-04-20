# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics
from animals.models import Kitten,Puppy
from animals.serializers import KittenSerialzer,PuppySerialzer


class KittenViewSet(viewsets.ModelViewSet):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerialzer


class PuppyView(generics.GenericAPIView):
    queryset = Puppy.objects.all()
    serializer_class = PuppySerialzer
