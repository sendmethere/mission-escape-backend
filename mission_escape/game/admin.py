from django.contrib import admin
from game.models import *

# Register your models here.
@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['id', 'nickname']
    list_display_links = ['id', 'nickname']

@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'user', 'created']
    list_display_links = ['id', 'name']

@admin.register(Escmap)
class EscAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'room']
    list_display_links = ['id', 'name']

@admin.register(Access)
class AccessAdmin(admin.ModelAdmin):
    list_display = ['id', 'code', 'target_map']
    list_display_links = ['id', 'code', 'target_map']