from django.shortcuts import render
from rest_framework import viewsets
from .models import Country,States
from .serializers import CountrySerializer,StateSerializer


class CountryViewSet(viewsets.ModelViewSet):
    queryset=Country.objects.all()
    serializer_class=CountrySerializer


class StateViewset(viewsets.ModelViewSet):
    queryset=States.objects.all()
    serializer_class=StateSerializer