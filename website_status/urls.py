from django.contrib import admin
from django.urls import path, include
from django.conf.urls import handler404
from checker.views import custom_404_view
from django.http import HttpResponseForbidden
from django.utils.deprecation import MiddlewareMixin


ALLOWED_ADMIN_IPS = ['127.0.0.1', '192.168.84.47', '89.249.63.66']


class AdminAccessControlMiddleware(MiddlewareMixin):
    def process_request(self, request):
        if request.path.startswith('/secret-admin/') and request.META['REMOTE_ADDR'] not in ALLOWED_ADMIN_IPS:
            return HttpResponseForbidden("Admin panelga kirish ruxsat etilmagan")


urlpatterns = [
    path('secret-vkjdsfsovsdklndsicslkdnscnslncsdncksnclksdn/', admin.site.urls),
    path('secret-checker/', include('checker.urls')),
]
