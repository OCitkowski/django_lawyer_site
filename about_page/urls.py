from django.urls import path
from .views import AboutView

app_name = 'bin'

urlpatterns = [
    path('', AboutView.as_view(), name='bin'),
]