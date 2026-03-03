"""
URL configuration for blogproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from . import views
from django.conf import settings
from django.conf.urls.static import static
from blogsapp import views as Blogview

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('category/', include('blogsapp.urls')),
    path('blogs/<slug:slug>/', Blogview.blogs, name='blogs'),
    #serach Endpoint
    path('blogsapp/search/', Blogview.search, name='search'),
    #Register Endpoint
    path('register/', views.register, name='register'),
    #Login End Point
    path('login/', views.login, name='login'),
    #Logout Endpoint
    path('logout/', views.logout, name='logout'),
    #dashboards
    path('dashboard/', include('dashboards.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
