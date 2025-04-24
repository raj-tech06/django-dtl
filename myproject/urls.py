"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from myapp import views
  

#   --------for img------------
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('home1/<int:pk>', views.home1, name='home1'),
    path('about/', views.about, name='about'),
    path('login/', views.login, name='login'),
    path('contact/', views.contact, name='contact'),
    path('contact1/<int:pk>', views.contact1, name='contact1'),

    path('register/', views.register, name='register'),
    path('registerdata/', views.registerdata, name='registerdata'),
    path('loginuser/', views.loginuser, name='loginuser'),
    path('dashboard/', views.dashboard, name='dashboard'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


