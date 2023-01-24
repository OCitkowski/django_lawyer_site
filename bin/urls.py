from django.urls import path
from .views import BinView

app_name = 'bin'

urlpatterns = [
    path('', BinView.as_view(), name='bin'),
]