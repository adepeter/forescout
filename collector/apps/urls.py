from django.urls import include, path

app_name = 'collector'

urlpatterns = [
    path('arps/', include('apps.arp.urls')),
]
