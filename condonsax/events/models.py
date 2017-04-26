from django.db import models
from django.utils import timezone

# Events is a model for upcoming concerts/lectures
class Event (models.Model):
    """
    Events will feed a listview of upcoming and past events
    title - name of the event
    event_date - date of the event
    pub_date - date the event will be published on the website
    event_image - image that will show on the event card
    """

    class Meta:
        verbose_name='Event'
        verbose_name_plural='Events'

    def __str__(self):
        return self.title

    title = models.CharField(max_length=50)
    slug = models.SlugField(max_length=50)
    event_date = models.DateField
    pub_date = models.DateField(default=timezone.now)
    event_image = models.ImageField(upload_to='media/%Y/%m/%d', blank=True)
