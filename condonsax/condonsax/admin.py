from django.contrib import admin

from home.admin import HomeAdmin
from home.models import HomePageText

class ChrisCondonAdmin(admin.sites.AdminSite):
    site_header = 'Chris Condon Administration'
    site_title = 'Chris Condon Administration'

condon_admin = ChrisCondonAdmin(name='admin')
condon_admin.register(HomePageText, HomeAdmin)