from django.shortcuts import render
from rest_framework import generics
from .serializers import DetailsSerializer
from .models import Details

class DetailsView(generics.CreateAPIView):
    queryset = Details.objects.all()
    serializer_class = DetailsSerializer

