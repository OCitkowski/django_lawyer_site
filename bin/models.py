from django.db import models
from solo.models import SingletonModel


class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default='Lawyer Didychenko')

    first_name = models.CharField(max_length=255, default='first name')
    second_name = models.CharField(max_length=255, default='second name')

    href_facebook = models.CharField(max_length=255, default='https://www.facebook.com/')
    href_instagram = models.CharField(max_length=255, default='https://www.instagram.com/')
    href_twitter = models.CharField(max_length=255, default='https://twitter.com/')

    foto = models.ImageField(verbose_name='Image', upload_to='images/%Y/%m/%d', blank=True)
    email = models.EmailField(max_length=255, default='yor_email@gmail.com')

    opening_hour = models.CharField(max_length=32, default='You can call me anytime')
    phone_number = models.CharField(max_length=32, default='+38096 111 11 11')
    address = models.CharField(max_length=32, default='My Street, Vinnytsia, Ukraine')

    title_about_me_footer = models.CharField(max_length=32, default='title_about_me')
    text_about_me_footer = models.TextField(max_length=500, default='''Lorem ipsum dolor sit amet, 
                        consectetur adipiscing elit. Quisque eu lectus a leo tristique
                        dictum nec non quam. Suspendisse convallis, tortor eu placerat rhoncus, lorem quam iaculis
                        felis, sed eleifend lacus neque id eros. Integer convallis volutpat ne'''
                                            )

    title_ge_in_touch_footer = models.CharField(max_length=32, default='title_ge_in_touch')

    page_about_title_our_journey = models.CharField(max_length=32, default='page_about_title_our_journey')

    page_practice_titl_our_practices_areas = models.CharField(max_length=32, default='page_practice_titl_our_practices_areas')
    page_practice_title_why_choose_us = models.CharField(max_length=32, default='page_practice_title_why_choose_us')
    page_practice_foto = models.ImageField(verbose_name='Image', upload_to='images/practice/%Y/%m/%d', blank=True)

    page_contact_title = models.CharField(max_length=32, default='page_contact_title')
    page_contact_title_location = models.CharField(max_length=32, default='page_contact_title_location')
    page_contact_title_phone = models.CharField(max_length=32, default='page_contact_title_phone')
    page_contact_title_email = models.CharField(max_length=32, default='page_contact_title_email')



    def __str__(self):
        return "Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"
