from django.urls import path

from . import site

urlpatterns = [
    path('', site.main),
]