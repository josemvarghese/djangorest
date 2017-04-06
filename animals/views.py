# from django.shortcuts import render
from rest_framework import viewsets
from animals.models import Kitten
from animals.serializers import KittenSerialzer


class KittenViewSet(viewsets.ModelViewSet):
    queryset = Kitten.objects.all()
    serializer_class = KittenSerialzer