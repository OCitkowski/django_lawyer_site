from django.db import models
from bin.utils import STATUS_CHOICES


class AboutUs(models.Model):
    """ information for theme"""
    title = models.CharField(max_length=100, unique=True, default='About me')
    text = models.TextField(max_length=2000, unique=True, default=''' Lorem ipsum dolor sit amet, consectetur adipiscing '
                                                                'elit. Phasellus nec pretium mi. Curabitur facilisis '
                                                                'ornare velit non vulputate. Aliquam metus tortor,'
                                                                'auctor id gravida condimentum, viverra quis sem.
                                                                Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
                                                                Phasellus nec pretium mi. 
                                                                Curabitur facilisis ornare velit non vulputate. 
                                                                Aliquam metus tortor, auctor id gravida condimentum, 
                                                                viverra quis sem. Curabitur non nisl nec nisi scelerisque maximus. 
                                                                Aenean consectetur convallis porttitor.
                                                                Aliquam interdum at lacus non blandit.''')
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')
    foto = models.ImageField(verbose_name='Image', upload_to='images/about/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ['title', 'text', 'date_added', 'foto', 'status']
        verbose_name = 'About me'
        verbose_name_plural = 'About me'

    def __str__(self):
        if len(self.title) >= 50:
            return f"{self.title[:150]}..."
        else:
            return f"{self.title[:150]}"


class AboutOurJourney(models.Model):
    """ information for theme"""
    title = models.CharField(max_length=100, unique=True, default='Learn About Us')
    text = models.TextField(max_length=2000, unique=True, default=''' Lorem ipsum dolor sit amet elit. Aliquam odio dolor,
                                                                    id luctus erat sagittis non. Ut blandit semper pretium. ''')
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')
    year = models.CharField(max_length=4, default='2000')
    is_left = models.BooleanField(default=True)

    class Meta:
        ordering = ['title', 'text', 'date_added', 'year', 'status']
        verbose_name = 'About year'
        verbose_name_plural = 'About year'

    def __str__(self):
        if len(self.title) >= 50:
            return f"{self.title[:150]}..."
        else:
            return f"{self.title[:150]}"
