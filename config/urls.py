"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from config import settings

handler404 = 'bin.views.custom_page_not_found_view'
# handler500 = 'basis_of_project.views.custom_error_view'
# handler403 = 'basis_of_project.views.custom_permission_denied_view'
# handler400 = 'basis_of_project.views.custom_bad_request_view'

urlpatterns = [
    # path('home/', include('home_page.urls')),
    path('bin/', include('bin.urls')),
    path('admin/', admin.site.urls),

]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:

    if settings.MEDIA_ROOT:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
