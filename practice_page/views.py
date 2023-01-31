from django.views.generic import TemplateView
from bin.utils import MENU
from .models import OurPracticesAreas, WhyChooseMe


class PracticeView(TemplateView):
    template_name = 'practice_page/practice.html'
    context_object_name = 'about'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['OurPracticesAreas'] = OurPracticesAreas.objects.filter(status='p')
        context['WhyChooseMe'] = WhyChooseMe.objects.filter(status='p')
        context['menu'] = MENU
        return context
