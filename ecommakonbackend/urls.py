from xml.etree.ElementInclude import include
from . import views
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('footer', views.footer, name="footer"),
]
