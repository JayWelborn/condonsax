from django.db import models
from django.utils import timezone

# Create your models here
class HomePageText (models.Model):
    """
    HomePageText class creates objects to allow client to choose text that displays on the home page
    'title' - text in browser tab
    'headline' - first line of text
    'sub_headlin' - second line of text
    'call_to_action' - text on link
    """

    class Meta:
        verbose_name='Home Page'
        verbose_name_plural = 'Home Page'

    def __str__(self):
        return self.headline

    title = models.CharField(max_length=40)
    headline = models.CharField(max_length=40)
    sub_headline = models.CharField(max_length=50)
    call_to_action = models.CharField(max_length=40)
    pub_date = models.DateField(default=timezone.now)


class HomePageTextFrench (models.Model):
    """
    Model for storing French home page in database
    'title' - text in browser tab
    'headline' - first line of text
    'sub_headlin' - second line of text
    'call_to_action' - text on link
    """

    class Meta:
        verbose_name='French Home Page'
        verbose_name_plural = 'French Home Page'

    def __str__(self):
        return self.headline

    title = models.CharField(max_length=40)
    headline = models.CharField(max_length=40)
    sub_headline = models.CharField(max_length=50)
    call_to_action = models.CharField(max_length=40)
    pub_date = models.DateField(default=timezone.now)


class HomePageTextGerman (models.Model):
    """
    Model for storing German home page in database
    'title' - text in browser tab
    'headline' - first line of text
    'sub_headlin' - second line of text
    'call_to_action' - text on link
    """

    class Meta:
        verbose_name='German Home Page'
        verbose_name_plural = 'German Home Page'

    def __str__(self):
        return self.headline

    title = models.CharField(max_length=40)
    headline = models.CharField(max_length=40)
    sub_headline = models.CharField(max_length=50)
    call_to_action = models.CharField(max_length=40)
    pub_date = models.DateField(default=timezone.now)


class HomePageTextSpanish (models.Model):
    """
    Object for storing Spanish home page in database
    'title' - text in browser tab
    'headline' - first line of text
    'sub_headlin' - second line of text
    'call_to_action' - text on link
    """

    class Meta:
        verbose_name='Spanish Home Page'
        verbose_name_plural = 'Spanish Home Page'

    def __str__(self):
        return self.headline

    title = models.CharField(max_length=40)
    headline = models.CharField(max_length=40)
    sub_headline = models.CharField(max_length=50)
    call_to_action = models.CharField(max_length=40)
    pub_date = models.DateField(default=timezone.now)


class About (models.Model):
    """
    AboutView stores info for "About Me" Page
    title - what displays in browser tab
    name - subject's name
    birth_date - subject's birth date
    bio - long bio
    about_image - image to float near bio
    pub_date - date page was most recently updated. defaults to creation date
    """

    class Meta:
        verbose_name='About Me Page'
        verbose_name_plural='About Me Page'

    def __str__(self):
        return 'About ' + self.name

    title = models.CharField(max_length=40)
    name = models.CharField(max_length=50)
    birth_date = models.DateField()
    bio = models.TextField(blank=True) # TODO install/configure TINYMCE
    # about_image = models.ImageField TODO install Pillow for ImageField use
    pub_date = models.DateField(default=timezone.now)


class Contact(models.Model):
    """
    Contact Page Details
    title - displays in browser tab
    facebook - link to facebook account
    youtube - link to youtube channel
    twitter - link to twitter account
    pub_date - date contact form was created/updated. If there are multiple, only the most recent
               one gets displayed
    """

    class Meta:
        verbose_name_plural = 'Contact Page'

    title = models.CharField(max_length=30)
    facebook = models.URLField(blank=True)
    youtube = models.URLField(blank=True)
    twitter = models.URLField(blank=True)
    pub_date = models.DateField(default=timezone.now)

    def __str__(self):
        return self.title
