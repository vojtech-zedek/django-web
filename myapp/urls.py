from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('overview/', views.overview, name='overview'),
    path('detail/<int:agency_id>/', views.detail, name='detail'),
]
