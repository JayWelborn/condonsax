from django.contrib import admin

from albums.models import Album

class AlbumInline(admin.TabularInline):
    model = Album
    ordering = ['pk']