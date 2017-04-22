from django.contrib import admin

from home.admin import HomeAdmin
from home.models import HomePageText, HomePageTextFrench, HomePageTextGerman, HomePageTextSpanish, About, Contact

class ChrisCondonAdmin(admin.sites.AdminSite):
    site_header = 'Chris Condon Administration'
    site_title = 'Chris Condon Administration'

condon_admin = ChrisCondonAdmin(name='admin')
condon_admin.register(HomePageText, HomeAdmin)
condon_admin.register(HomePageTextFrench, HomeAdmin)
condon_admin.register(HomePageTextGerman, HomeAdmin)
condon_admin.register(HomePageTextSpanish, HomeAdmin)
condon_admin.register(About)
condon_admin.register(Contact)