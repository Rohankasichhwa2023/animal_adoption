"""
URL configuration for animal_adoption project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.views.generic import RedirectView
from adoption.views import adoption_form
from django.conf import settings
from django.conf.urls.static import static
from adoption.views import animal_list 

urlpatterns = [
    path('', animal_list, name='animal_list'),  # Set the animal_list view as the default page
    path('admin/', admin.site.urls),  # Include Django's admin URLs
    path('adoption/', include('adoption.urls')),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)