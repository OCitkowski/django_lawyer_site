from config import settings
from .forms import ContactForm
from django.views.generic.edit import FormView
from bin.utils import MENU
from django.utils import timezone
from bin.models import SiteConfiguration
from django.core.mail import EmailMessage, BadHeaderError
from django.shortcuts import HttpResponse, redirect
from django.core.mail import send_mail


class ContactFormView(FormView):
    template_name = 'contact_page/contact.html'
    form_class = ContactForm
    success_url = '/contact/'

    def form_valid(self, form):
        self.send_email(form)

        # first_name = form.cleaned_data.get('first_name')
        # # first_name = self.request.POST.get('first_name')
        # last_name = self.request.POST.get('last_name')
        # email_address = self.request.POST.get('email_address')
        # message = self.request.POST.get('message')
        #
        # send_mail(subject=first_name,
        #           message=message,
        #           from_email=settings.EMAIL_HOST_USER,
        #           recipient_list=[email_address, ],
        #           auth_user='o.citkowski@yahoo.com',
        #           auth_password='H4UEp47PBU8CjL7',
        #           fail_silently=False, )
        print('Ok')
        return super().form_valid(form)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['first'] = SiteConfiguration.objects.all().first()
        context['now'] = timezone.now()
        context['menu'] = MENU
        return context

    def send_email(self, form):

        try:
            name = form.cleaned_data.get('first_name')
            phone = self.request.POST.get('phone')
            email_address = self.request.POST.get('email_address')
            message = self.request.POST.get('message')

            recipient_list = [email_address, ]
            msg_email = EmailMessage(
                subject=f'Hello {name} ',
                from_email=settings.EMAIL_HOST_USER,
                body=message,
                to=recipient_list,
                fail_silently=False
            )
            msg_email.send()
        except BadHeaderError:
            return HttpResponse('Invalid header found.')
        return redirect("contact_page:contact")
