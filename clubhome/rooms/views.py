from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, TemplateView

from rooms.models import Room, Moderator


class RoomCreateWithUserView(TemplateView):
    template_name = "rooms/room_form.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        data = request.POST

        room = Room.objects.create(
            topic=data['topic']
        )

        moderator = Moderator()
        moderator.room = room
        moderator.user = request.user
        moderator.save()

        return redirect('room-list')


class RoomCreateView(CreateView):
    model = Room
    fields = ['topic']
    success_url = reverse_lazy('room-list')


class RoomListView(ListView):
    queryset = Room.objects.all()
    context_object_name = 'rooms'