from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponseNotFound

admin.autodiscover()

urlpatterns = [
    path('secret-admin/', admin.site.urls),
    path('secret-checker/', include('checker.urls')),
]


def custom_page_not_found(request, exception=None):
    return HttpResponseNotFound('Page not found')

handler404 = 'websites_url.urls.custom_page_not_found'
