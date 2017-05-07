from django.db import models
from django.utils import timezone

from tinymce import HTMLField

from .fields import AudioFileField


# Albums is a model for published albums
class Album (models.Model):
    """
    Albums will contain the following
    title - album title
    slug - title slugified for urls
    cover - cover image
    tracks - reverse lookup of foreign key from track object
    album_itunes - url to buy album on itunes
    album_amazon - url to buy album on amazon
    release_date - date album was (or will be) released
                   albums home page will show albums ordered from newest to oldest
    
    """

    class Meta:
        verbose_name='Album'
        verbose_name_plural='Albums'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Defines primary key and slug as components of url
        """
        args = (self.pk, self.slug)
        return reverse(self, args)

    title = models.CharField(max_length=100)
    slug = models.SlugField('URL', max_length=100)
    cover = models.ImageField('Cover Photo 400x400px recommended', upload_to='media/%Y/%m/%d', blank=True, null=True)
    release_date = models.DateField(default=timezone.now)
    # tracks = related name for AlbumTrack objects with foreign key matching current album
    album_itunes = models.URLField(' iTunes URL:', blank=True, null=True)
    album_amazon = models.URLField(' Amazon URL:', blank=True, null=True)
    write_up = HTMLField('Album Description', blank=True, null=True)


# Composer is a model for composers of pieces
class Composer (models.Model):
    """
    Composer will hold data for composers of pieces.
    Created so the same composer can be represented multiple times without storing information multiple times
    name - Composer's Name
    slug - Name slugified for url
    birth_date - composer's birth date (if known)
    headshot - composer's picture (if available)
    """

    class Meta:
        verbose_name='Composer'
        verbose_name_plural='Composers'

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        """
        Defines slug as main component of url
        """
        args = (self.slug)
        return reverse(self, args)

    name = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    birth_date = models.DateField(default=timezone.now, blank=True, null=True)
    headshot = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, null=True)
            

# AlbumTrack is a model for individual tracks
class AlbumTrack (models.Model):
    """
    Album Track will contain detailed information about each Track on an album
    title - name of track
    album - album on which each track appears
    composer - composer of each piece
    composition_date - date piece was published
    audio_sample - mp3 audio sample
    track_itunes - url to buy track on itunes
    track_amazon - url to buy track on amazon
    """

    class Meta:
        verbose_name='Track'
        verbose_name_plural='Tracks'

    def __str__(self):
        return self.title

    title = models.CharField(max_length=50)
    album = models.ForeignKey(Album, related_name='tracks')
    composer = models.ForeignKey(Composer, related_name='pieces')
    composition_date = models.DateField(default=timezone.now, blank=True, null=True)
    audio_sample = AudioFileField(max_upload_size=10485760)
