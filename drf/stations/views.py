# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from stations.models import A136
from stations.serializers import StationSerializer
from rest_framework import generics

class StationList(generics.ListCreateAPIView):
    queryset = A136.objects.all()
    serializer_class = StationSerializer

class StationDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = A136.objects.all()
    serializer_class = StationSerializer
