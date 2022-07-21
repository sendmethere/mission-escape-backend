from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from mission_escape.game.models import *
from mission_escape.game.serializers import *

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    
class RoomViewSet(viewsets.ModelViewSet):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer

    
class EscmapViewSet(viewsets.ModelViewSet):
    queryset = Escmap.objects.all()
    serializer_class = EscmapSerializer
    
class AccessViewSet(viewsets.ModelViewSet):
    queryset = Access.objects.all()
    serializer_class = AccessSerializer