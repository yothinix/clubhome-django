from django.db import models
from rest_framework import serializers

from rooms.models import Room


class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = ['id', 'topic', 'is_active', 'room_moderator', 'room_listener']
        depth = 2


class RoomCreateSerializer(serializers.Serializer):
    topic = serializers.CharField(required=True)
    moderator = serializers.ListField(child=serializers.CharField(required=True), min_length=1, allow_empty=False)