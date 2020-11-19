from django.urls import include, path

urlpatterns = [
    path('', include('apps.arp.urls')),
]
