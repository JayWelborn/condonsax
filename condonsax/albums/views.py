from django.views import generic
from django.utils import timezone

from .models import Album, Composer


class AlbumListView (generic.ListView):
    """
    AlbumListView is a list of albums displayed as cards
    Template will be given liist of all distinct album objects
    ordered by reverse release date (newest first) for iteration.
    """

    template_name = 'albums/albumlist.html'
    context_object_name = 'album_list'
    model = Album
    paginate_by = 6

    def get_queryset(self):
        """
        returns list of albums with release dates in the past sorted
        by release date (newest first)
        """
        albums = Album.objects.distinct()
        released_albums = albums.filter(release_date__lte=timezone.now())
        return released_albums.order_by('-release_date')
