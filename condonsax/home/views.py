from django.views.generic import TemplateView

from .models import HomePageText

# Create your views here.
class HomePageView(TemplateView):
    """
    HomePageView is a class for displaying the home page.
    It will fetch the most recent HomePageText object
    and pass it to 'home/index.html'
    """

    template_name = 'home/index.html'

    def get_context_data(self, **kwargs):
        """
        Return data from most recent update to home info in database.
        """
        context = super(HomePageView, self).get_context_data(**kwargs)
        try:
            context['home'] = HomePageText.objects.latest('pub_date')
        except DoesNotExist:
            pass
        return context
