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
        verbose_name_plural = 'Home Pages'

    def __str__(self):
        return self.headline

    title = models.CharField(max_length=40)
    headline = models.CharField(max_length=40)
    sub_headline = models.CharField(max_length=50)
    call_to_action = models.CharField(max_length=40)
    pub_date = models.DateField(default=timezone.now)