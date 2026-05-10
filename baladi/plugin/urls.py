from django.urls import path, include, re_path
from django.contrib import admin
from . import views
from .views import Myuserview

urlpatterns = [
    re_path(r'^(?P<id_key>[^/]+)/api/$',Myuserview.as_view()),
    path("", views.index, name = "index"),
    ]
