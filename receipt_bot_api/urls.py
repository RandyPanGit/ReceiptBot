from django.urls import path

from . import views

urlpatterns = [
    path('months', views.YourView.as_view()),
]
