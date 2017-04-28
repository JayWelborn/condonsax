from django.views.generic import TemplateView
from django.utils import timezone

from .models import Event


class EventView (TemplateView):
    """
    EventView fetches two different lists of Event objects.
    future_events is a list of events with an event date in the future
    past_events is a list of events with an event date in the past
    events.html will make a large list with events styled differently
    """

    template_name = 'events/event.html'

    def get_context_data(self, **kwargs):
        context = super(EventView, self).get_context_data(**kwargs)
        # get list of events marked as publishable
        published_events = Event.objects.filter(pub_date__lte=timezone.now())
        
        # list of events in the future
        future_events = published_events.filter(event_date__gte=timezone.now())
        
        # list of events in the past
        past_events = published_events.filter(event_date__lt=timezone.now())

        # add lists to context
        context['future_events'] = future_events.order_by('-pub_date')
        context['past_events'] = past_events.order_by('-pub_date')
        return context