from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('logout/', views.log_out, name='log_out'),
    path('data', views.data, name='data'),
    path('loaddata', views.loaddata, name='loaddata'),
    path('catalog', views.catalog, name='catalog'),
]