from django.shortcuts import render
from News.models import News
from News.serializers import NewsSerializer
from rest_framework import viewsets

class NewsViewset(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer