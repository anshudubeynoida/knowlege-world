"""eshop URL Configuration

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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from mainApp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('post/<str:mc>/<str:sc>/<str:br>/',views.shop),
    path('blog/<str:posturl>/',views.Pblog),
    # path('post/',views.post),
    path('search/',views.searchPage),
    path('contact/',views.contactPage),
    path('facts/',views.facts),
    path('life/<str:mc>/<str:sc>/<str:br>/',views.life),
    path('tech/<str:mc>/<str:sc>/<str:br>/',views.tech),
    path('nature/<str:mc>/<str:sc>/<str:br>/',views.nature),
    path('mobile/<str:mc>/<str:sc>/<str:br>/',views.mobile),

    
    
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
