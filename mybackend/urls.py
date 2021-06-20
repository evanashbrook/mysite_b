from django.urls import path
from . import views

urlpatterns = [
    path('', views.AppListCreate.as_view()),
]
