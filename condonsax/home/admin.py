from django.contrib import admin

class HomeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Title', {'fields': ['title',]}),
        ('Publication Date', {'fields': ['pub_date']}),
        ('Text', {'fields': ['headline', 'sub_headline', 'call_to_action']}),
    ]
    list_display = ('title', 'pub_date')
    list_filter = ['pub_date']
