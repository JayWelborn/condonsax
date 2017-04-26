from django.contrib import admin

from .models import Event

# Register your models here.
class EventAdmin(admin.ModelAdmin)
    """
    Admin Page class for managing Events
    """
    fieldsets = [
        ('Title', {'fields': ['title', 'slug']}),
        ('Event and Publication Dates', {'fields': ['event_date', 'pub_date']}),
        ('Image', {'fields': ['event_image']}),
    ]
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']