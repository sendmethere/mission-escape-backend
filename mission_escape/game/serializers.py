from rest_framework import serializers
from .models import *

# class NoticeSerializer(serializers.ModelSerializer):
#    class Meta:
#        model = Notice
#        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = '__all__'

class EscmapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Escmap
        fields = '__all__'

class AccessSerializer(serializers.ModelSerializer):
    class Meta:
        model = Access
        fields = '__all__'