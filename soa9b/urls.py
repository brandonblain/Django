"""soa9b URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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

from soa9b.views import hello_world
from services import views as serv_views
from api.api import UserAPI
from api.api import ProductsListAPI

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello_world),
    # path('services/', serv_views.showTemplate),
    path('games/create/', serv_views.createSubject), 
    path('games/lista/', serv_views.listaGames), 
    path('games/venta/', serv_views.venta), 
    path('index/', serv_views.index), 
    # path('services/', serv_views.showTemplate,name='index'),
    # path('services/create', serv_views.createSubject,name='create_services'),
    path('api/user/create', UserAPI.as_view()),
    path('api/products', ProductsListAPI.as_view(),name='api_products_list'),
]
