from django.contrib import admin


# Register your models here.
class EventAdmin(admin.ModelAdmin):
    """
    Admin Page class for managing Events
    """
    fieldsets = [
        ('Title', {'fields': ['title', 'slug']}),
        ('Event and Publication Dates', {'fields': ['event_date', 'pub_date']}),
        ('Event Time', {'fields': ['event_time']}),
        ('Image', {'fields': ['event_image']}),
        ('Location and extra Information', {'fields': ['location','write_up']}),
    ]
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('location', 'event_date', 'title',)
    list_filter = ['event_date']