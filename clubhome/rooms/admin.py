from django.contrib import admin

from rooms.models import Room, Moderator, Listener


class ModeratorInline(admin.TabularInline):
    model = Moderator

class ListenerInline(admin.StackedInline):
    model = Listener

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['topic', 'is_active']
    search_fields = ['topic']
    list_filter = ['is_active']
    inlines = [ModeratorInline, ListenerInline]


admin.site.register(Moderator)
admin.site.register(Listener)
