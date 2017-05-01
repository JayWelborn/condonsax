from django.db import models
from django.utils import timezone
from django.core.validators import MinValueValidator, MaxValueValidator

from tinymce import HTMLField


class Address (models.Model):
    """
    Address will be the address of each event. Each event can have only one address, but each address
    can be used multiple times in the case of repeat performances
    street_address - street name and number
    city - event city
    postal_code - zip code of performance
    state_or_country - state or country of performance
    """

    class Meta:
        verbose_name='Performance Venue'
        verbose_name_plural='Performance Venues'

    def __str__(self):
        return '{}\n{}, {}'.format(self.venue_name, self.city, self.state_or_country)

    venue_name = models.CharField(max_length=100, blank=True, null=True)
    street_address = models.CharField(max_length=40)
    city = models.CharField(max_length=40)
    postal_code = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(9999999)])
    state_or_country = models.CharField(max_length=2)

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
        return self.title + str(self.location)

    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    event_date = models.DateField(default=timezone.now)
    event_time = models.TimeField(default=timezone.now)
    pub_date = models.DateField(default=timezone.now)
    event_image = models.ImageField(upload_to='media/%Y/%m/%d', blank=True, null=True)
    location = models.ForeignKey(Address, blank=True, null=True, default=1)
    write_up = HTMLField('Event Write Up', blank=True, null=True)
