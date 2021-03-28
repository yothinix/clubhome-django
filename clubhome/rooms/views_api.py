from django.contrib.auth import get_user_model

from rest_framework import serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Moderator, Room
from .serializers import RoomCreateSerializer, RoomSerializer

User = get_user_model()

class RoomViewSet(ModelViewSet):
    queryset = Room.objects.all()

    serializers = {
        'default': RoomSerializer,
        'create': RoomCreateSerializer
    }

    def get_serializer_class(self):
        return self.serializers.get(self.action, self.serializers['default'])

    def create(self, request, *args, **kwargs):
        serializer = RoomCreateSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        room_recipe = serializer.validated_data

        room = Room.objects.create(topic=room_recipe.get('topic'))

        for moderator_user in room_recipe.get('moderator'):
            user = User.objects.get(username=moderator_user)
            Moderator.objects.create(room=room, user=user)
        
        response_serializer = RoomSerializer(room)
        headers = self.get_success_headers(serializer.data)
        return Response(response_serializer.data, status=status.HTTP_201_CREATED, headers=headers)
