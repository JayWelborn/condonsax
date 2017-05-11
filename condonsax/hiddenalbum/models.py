from django.db import models

from albums.models import Album

class HiddenAlbum(models.Model):
    
    album = models.ForeignKey(Album)
    slug = models.SlugField('URL slug', max_length=100, db_index=True)

    def get_absolute_url(self):
        """
        Defines primary key and slug as components of url
        """
        args = (self.slug)
        return reverse(self, args)

    def __str__(self):
        return self.album.title
