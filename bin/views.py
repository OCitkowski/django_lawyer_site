from django.shortcuts import render
from django.views.generic import TemplateView
from bin.utils import MENU
from django.utils import timezone
# from .models import SiteConfiguration


def custom_page_not_found_view(request, exception):
    return render(request, "bin/errors/404.html", {})


#
# def custom_error_view(request, exception=None):
#     return render(request, "/bin/errors/500.html", {})
#
#
# def custom_permission_denied_view(request, exception=None):
#     return render(request, "bin/errors/403.html", {})
#
#
# def custom_bad_request_view(request, exception=None):
#     return render(request, "bin/errors/400.html", {})


class BinView(TemplateView):
    # model = SiteConfiguration
    template_name = 'bin/index.html'
    context_object_name = 'basis'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['now'] = timezone.now()
        context['menu'] = MENU
        return context
