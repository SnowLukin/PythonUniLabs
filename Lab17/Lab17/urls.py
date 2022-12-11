from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('accounts/', include('django.contrib.auth.urls')),
    path('djangoTest/', include('djangoTest.urls')),
    path('admin/', admin.site.urls)
]