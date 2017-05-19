# Standard library imports
from datetime import timedelta

# Django imports
from django.db import models
from django.utils import timezone
from django.urls import reverse

from tinymce import HTMLField


class Project(models.Model):
    """
    Project is a class that allows a blog entry to be published about a
    completed major project. Projects can include albums, commissioned
    pieces, or important performances. Projects are to be presented in the
    style of a blog, and allow embedded images and videos when needed.
    title - Title of project
    slug - url slug
    header_image - image to display at top of screen
    pub_date - Date entry was published
    body - main text of project entry
    tags - related topics
    """

    class Meta:
        verbose_name='Project'
        verbose_name_plural='Projects'


    title = models.CharField(max_length=100, unique=True)
    slug = models.SlugField('URL slug', max_length=100, unique=True)
    header_image = models.ImageField('Header Image', upload_to='media/%Y/%m/%d', blank=True)
    pub_date = models.DateTimeField('date published', default=timezone.now)
    body = HTMLField('Body')
    tags = models.ManyToManyField('Tag', related_name='projects', blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        """
        Defines primary key and slug as components of url
        """
        args = (self.pk, self.slug)
        return reverse(self, args)

    def was_published_recently(self):
        now = timezone.now()
        return now - timedelta(days=30) <= self.pub_date <= now

    was_published_recently.admin_order_field = 'pub_date'
    was_published_recently.boolean = True
    was_published_recently.short_description = 'Published recently?'


class Tag(models.Model):
    title = models.CharField(max_length=100, db_index=True)
    slug = models.SlugField('URL slug', max_length=100, db_index=True)

    def get_absolute_url(self):
        """
        Defines primary key and slug as components of url
        """
        args = (self.pk, self.slug)
        return reverse(self, args)

    def __str__(self):
        return self.title