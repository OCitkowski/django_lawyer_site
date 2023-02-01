from django.db import models
from bin.utils import STATUS_CHOICES


class Carousel(models.Model):
    """ information for theme"""
    is_first = models.BooleanField(default=False)
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default='p')

    title = models.CharField(max_length=100, unique=True, default='We fight for your justice')
    text = models.TextField(max_length=200, unique=True,
                            default='Lorem ipsum dolor sit amet elit. Mauris odio mauris...')
    date_added = models.DateTimeField(auto_now_add=True)

    foto_carousel = models.ImageField(verbose_name='Image', upload_to='images/home/%Y/%m/%d', blank=True)

    class Meta:
        ordering = ['title', 'text', 'date_added', 'is_first', 'status', 'foto_carousel']
        verbose_name = 'Carousel'
        verbose_name_plural = 'Carousel'

    def __str__(self):
        if len(self.title) >= 50:
            return f"{self.title[:150]}..."
        else:
            return f"{self.title[:150]}"
