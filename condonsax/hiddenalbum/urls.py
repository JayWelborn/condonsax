# Django imports
from django.conf.urls import url

# Relative imports
from .views import HiddenAlbumHomeView, HiddenAlbumDetailView

app_name = 'hiddenalbum'
urlpatterns = [
    # ex: /hiddenalbum/album-slug-goes-here
    url(r'^(?P<slug>[-\w\d]+)/$', HiddenAlbumDetailView.as_view(), name='detail'),
    # ex: /hiddenalbum
    url(r'^$', HiddenAlbumHomeView.as_view(), name='hiddenalbum'),
]
