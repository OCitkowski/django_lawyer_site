from django.views.generic import TemplateView
from bin.utils import MENU
from .models import Carousel, ReviewFromClient
from about_page.models import AboutUs
from practice_page.models import OurPracticesAreas, WhyChooseMe


class HomeView(TemplateView):
    template_name = 'home_page/home.html'
    context_object_name = 'home'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Carousel'] = Carousel.objects.filter(status='p')
        context['WhyChooseMe'] = WhyChooseMe.objects.filter(status='p')
        context['AboutUs'] = AboutUs.objects.filter(status='p')
        context['ReviewFromClient'] = ReviewFromClient.objects.filter(status='p')
        context['OurPracticesAreas'] = OurPracticesAreas.objects.filter(status='p')
        context['WhyChooseMe'] = WhyChooseMe.objects.filter(status='p')
        context['menu'] = MENU
        return context
