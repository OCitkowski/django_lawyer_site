from django.views.generic import TemplateView
from bin.utils import MENU
from .models import Carousel


class HomeView(TemplateView):
    template_name = 'home_page/home.html'
    context_object_name = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Carousel'] = Carousel.objects.filter(status='p')
        # context['AboutUs'] = AboutUs.objects.filter(status='p')
        context['menu'] = MENU
        return context
