from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from checker.views import custom_404_view

handler404 = custom_404_view

urlpatterns = [
    path('secret-admin/', admin.site.urls),
    path('secret-checker/', include('checker.urls')),
]
