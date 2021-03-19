from django.contrib.auth import get_user_model
from django.db import models

class Room(models.Model):
    topic = models.CharField(null=False, blank=False, max_length=256)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return f'Room {self.id}: {self.topic} (Listener: {self.room_listener.count()}) (Moderator: {self.room_moderator.count()})'

User = get_user_model()

class Moderator(models.Model):
    room = models.ForeignKey(Room, related_name='room_moderator', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_moderator', on_delete=models.CASCADE)

    def __str__(self):
        return f'Moderator: {self.room.topic} - {self.user.name}'

class Listener(models.Model):
    room = models.ForeignKey(Room, related_name='room_listener', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='user_listener', on_delete=models.CASCADE)

    def __str__(self):
        return f'Listener: {self.room.topic} - {self.user.name}'
