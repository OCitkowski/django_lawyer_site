from django.urls import path
from .views import PracticeView

app_name = 'practice'

urlpatterns = [
    path('', PracticeView.as_view(), name='practice'),
]