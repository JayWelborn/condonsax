from django.contrib import admin


# Add projects entries
class ProjectAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title', 'slug']}),
        ('Publication Date', {'fields': ['pub_date']}),
        ('Header', {'fields': ['header_image']}),
        ('Entry', {'fields': ['body', 'tags']}),
    ]
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']