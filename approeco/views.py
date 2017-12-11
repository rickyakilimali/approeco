from django.views import generic
from django.core.urlresolvers import reverse_lazy


class HomePageView(generic.TemplateView):
    template_name = 'home.html'
        