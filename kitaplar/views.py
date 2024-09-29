from django.shortcuts import render
from rest_framework import viewsets
from .models import Kitap
from .serializers import KitapSerializer

class KitapViewSet(viewsets.ModelViewSet):
    queryset = Kitap.objects.all()
    serializer_class = KitapSerializer

