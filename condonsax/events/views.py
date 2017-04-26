from django.views.generic import ListView

from .models import Event


class EventView (ListView):
    """
    EventView fetches two different lists of Event objects.
    future_events is a list of events with an event date in the future
    past_events is a list of events with an event date in the past
    events.html will make a large list with events styled differently
    """

    template_name = 'events/event.html'
    paginate_by = 5

    def get_context_data(self, **kwargs):
        context = super(EventView, self).get_context_data(**kwargs)
        published_events = Events.objects.filter(pub_date__lte=timezone.now())
        sorted_events = published_events.order_by('-pub_date')