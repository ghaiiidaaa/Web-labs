"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import include, path
from django.views.generic import RedirectView
from apps.bookmodule import views as book_views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('books/', include('apps.bookmodule.urls')),  # Includes bookmodule URLs
    path('users/', include('apps.usermodule.urls')),
    path('', RedirectView.as_view(url='/books/')),  # Redirect root URL to /books/
    path('students/', include('apps.bookmodule.urls')),
     path('students2/', include('apps.bookmodule.urls')), 
 path('images/', include('apps.bookmodule.urls')),  # Routes to images URLs
]

if settings.DEBUG:  # Only serve media files during development
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)