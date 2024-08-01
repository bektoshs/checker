from django.http import HttpResponseForbidden

ALLOWED_ADMIN_IPS = ['127.0.0.1', '89.249.63.66', '192.168.84.47']


class AdminAccessControlMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.path.startswith('/admin/') and request.META['REMOTE_ADDR'] not in ALLOWED_ADMIN_IPS:
            return HttpResponseForbidden("Admin panelga kirish ruxsat etilmagan")
        return self.get_response(request)
