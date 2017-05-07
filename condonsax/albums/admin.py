from django.contrib import admin

from .models import AlbumTrack


class TrackInline(admin.TabularInline):
    model = AlbumTrack
    extra = 0
    ordering = ['pk']


class AlbumAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title', 'slug']}),
        ('Publicity Information', {'fields': ['cover', 'release_date',]}),
        ('Online Retailers', {'fields': ['album_itunes', 'album_amazon']}),
        ('Write Up', {'fields': ['write_up']})
    ]
    list_display = ('title', 'release_date')
    list_filter = ['release_date']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [TrackInline]
