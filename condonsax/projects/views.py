# Django imports
from django.views import generic
from django.utils import timezone

# Relative imports
from .models import Project, Tag


# Create your views here.
class IndexView(generic.ListView):
    """
    View for displaying list of projects on a home screen.
    """
    template_name = 'projects/projects.html'
    context_object_name = 'project_list'
    model = Project
    paginate_by = 6

    def get_queryset(self):
        """
        Return projects sorted by date
        """
        projects = Project.objects.distinct()
        return projects.filter(
            pub_date__lte=timezone.now()
        ).order_by('-pub_date')


class DetailView(generic.DetailView):
    """
    View single project
    """
    model = Project
    template_name = 'projects/detail.html'


class TagListView(generic.ListView):
    """
    View all projects assiciated with a certain tag
    """
    model = Tag
    template_name = 'projects/tag_list.html'
    context_object_name = 'tag_list'
    paginate_by = 6
    paginate_orphans = 2

    def get_queryset(self):
        return Tag.objects.distinct()


class TagDetailView(generic.DetailView):
    model = Tag
    template_name = 'projects/tag_detail.html'
    context_object_name = 'tag'
    paginate_by = 6

