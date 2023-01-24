from django.db import models
from solo.models import SingletonModel


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default='Site Name')

    first_name = models.CharField(max_length=255, default='first name')
    second_name = models.CharField(max_length=255, default='second name')

    href_facebook = models.CharField(max_length=255, default='https://www.facebook.com/')
    href_instagram = models.CharField(max_length=255, default='https://www.instagram.com/')

    foto = models.ImageField(verbose_name='Image', upload_to='images/%Y/%m/%d', blank=True)
    email = models.EmailField(max_length=255, default='yor_email@gmail.com')

    opening_hour = models.CharField(max_length=32, default='8:00 - 22:00')
    phone_number = models.CharField(max_length=32, default='+38096 111 11 11')
    address = models.CharField(max_length=32, default='My Street, Vinnytsia, Ukraine')

    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"
