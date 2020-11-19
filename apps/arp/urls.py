from django.urls import path

from . import apiviews

urlpatterns = [
    path('', apiviews.ARPListAPIView.as_view(), name='arp_list'),
]
