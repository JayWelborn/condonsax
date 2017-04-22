from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import TemplateView, FormView

from .models import HomePageText, About, Contact
from .forms import ContactForm

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
        context['home'] = HomePageText.objects.latest('pub_date')
        return context


class AboutView (TemplateView):
    """
    AboutView displays about page.
    It will fetch the most recent About object
    and pass it to 'home/about.html'
    """

    template_name = 'home/about.html'

    def get_context_data(self, **kwargs):
        """
        Return data from most recent update to about me page in database
        """
        context = super(AboutView, self).get_context_data(**kwargs)
        context['about'] = About.objects.latest('pub_date')
        return context


class ContactView(SuccessMessageMixin, FormView):
    """
    Display Contact page
    Displays ContactForm from .forms
    Gets latest Contact object from .models
    """
    template_name = 'home/contact.html'
    form_class = ContactForm
    success_url = '/contact/'
    success_message = 'Thanks for the Email!'

    def get_context_data(self, **kwargs):
        """
        Get most recent Contact object
        """
        context = super(ContactView, self).get_context_data(**kwargs)
        context['contact'] = Contact.objects.latest('pub_date')
        return context

    def form_valid(self, form):
        """
        Sends email and displays success message when a valid form
        is submitted.
        """
        form.send_email()
        return super(ContactView, self).form_valid(form)
