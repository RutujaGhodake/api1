from django.shortcuts import render
from rest_framework import viewsets
from api.models import user,post,like
from api.serializers import userserializers,postserializers,likeserializers

# Create your views here.

class userviewset(viewsets.ModelViewSet):
    queryset = user.objects.all()
    serializer_class = userserializers

class postviewset(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = postserializers

class likeviewset(viewsets.ModelViewSet):
    queryset = like.objects.all()
    serializer_class = likeserializers


