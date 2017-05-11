from django.contrib import admin

# Home Admin and Models
from home.admin import HomeAdmin
from home.models import HomePageText, HomePageTextFrench, HomePageTextGerman, HomePageTextSpanish, About, Contact

# Events Admin and Models
from events.admin import EventAdmin
from events.models import Event, Address

# Albums Admin and Models
from albums.models import Composer, Album
from albums.admin import AlbumAdmin

# Projects Admin and Models
from projects.models import Project, Tag
from projects.admin import ProjectAdmin

# Secret Album Admin and Model
from hiddenalbum.models import HiddenAlbum

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
condon_admin.register(Event, EventAdmin)
condon_admin.register(Address)
condon_admin.register(Album, AlbumAdmin)
condon_admin.register(Composer)
condon_admin.register(Project, ProjectAdmin)
condon_admin.register(Tag)
condon_admin.register(HiddenAlbum)