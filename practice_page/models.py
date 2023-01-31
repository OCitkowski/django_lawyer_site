from django.db import models
from bin.utils import STATUS_CHOICES, ICON_Practice_CHOICES


class OurPracticesAreas(models.Model):
    """ information for theme"""
    title = models.CharField(max_length=100, unique=True, default='Our Practices Areas')
    text = models.TextField(max_length=2000, unique=True, default=''' Lorem ipsum dolor sit amet elit. 
                                                    Phasellus nec pretium mi. 
                                                    Curabitur facilisis ornare velit non .''')
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')
    icon = models.CharField(max_length=25, choices=ICON_Practice_CHOICES, default="far fa-smile")

    class Meta:
        ordering = ['title', 'text', 'date_added', 'icon', 'status']
        verbose_name = 'Our Practices Areas'
        verbose_name_plural = 'Our Practices Areas'

    def __str__(self):
        if len(self.title) >= 50:
            return f"{self.title[:150]}..."
        else:
            return f"{self.title[:150]}"

class WhyChooseMe(models.Model):
    """ information for theme"""
    title = models.CharField(max_length=100, unique=True, default='Why Choose Us')
    text = models.TextField(max_length=2000, unique=True, default=''' Why Choose Us Lorem ipsum dolor sit amet elit. 
                                                    Phasellus nec pretium mi. 
                                                    Curabitur facilisis ornare velit non .''')
    date_added = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')
    icon = models.CharField(max_length=25, choices=ICON_Practice_CHOICES, default="far fa-smile")

    class Meta:
        ordering = ['title', 'text', 'date_added', 'icon', 'status']
        verbose_name = 'Why Choose Us'
        verbose_name_plural = 'Why Choose Us'

    def __str__(self):
        if len(self.title) >= 50:
            return f"{self.title[:150]}..."
        else:
            return f"{self.title[:150]}"


