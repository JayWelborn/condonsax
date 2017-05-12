from django.views import generic

from .models import HiddenAlbum


class HiddenAlbumHomeView(generic.ListView):
    """
    Class for viewing a list of hidden albums for venues/reviewers
    """
    template_name = 'hiddenalbum/hiddenalbum.html'
    context_object_name = 'album_list'
    model = HiddenAlbum
    paginate_by = 6

    def get_queryset(self):
        """
        Return projects sorted by date
        """
        hidden_albums = HiddenAlbum.objects.distinct()
        return hidden_albums.order_by('-pk')


# Create your views here.
class HiddenAlbumDetailView(generic.DetailView):
    """
    View full tracks of a particular album
    """
    model = HiddenAlbum
    template_name = 'hiddenalbum/detail.html'