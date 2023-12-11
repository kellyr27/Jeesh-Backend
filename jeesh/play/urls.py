from django.urls import path
from . import views

urlpatterns = [
    path('initialize/', views.InitializeView.as_view(), name='initialize'),
    path('', views.IndexView.as_view(), name='index'),
    # Add more paths here
]
