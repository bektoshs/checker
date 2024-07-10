from django.http import JsonResponse
from opentelemetry import trace
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from django.views.decorators.csrf import csrf_exempt
from .models import Website
from .serializers import WebsiteSerializer

tracer = trace.get_tracer(__name__)
@csrf_exempt
def check_website(request):
    with tracer.start_as_current_span("check_website_operation"):
        if request.method == 'POST':
            address = request.POST.get('address')
            status = request.POST.get('status')

            if not address:
                return JsonResponse({'xato': 'Manzil kerak'}, status=400)

            print(f"Kiritilgan address: {address}")
            print(f"Kiritilgan status: {status}")

            website, created = Website.objects.get_or_create(address=address)

            if created:
                if status:
                    website.status = status
                elif ((address.endswith('.asakabank.uz') or address.endswith('.askb.uz')) or
                      (address == ('asakabank.uz') or address.endswith('askb.uz'))):
                    website.status = 'original'
                elif ((address.startswith('asakabank.') and address.endswith('.uz')) or
                      (address.startswith('askb.') and address.endswith('.uz'))):
                    website.status = 'fake'
                else:
                    website.status = 'not_checked'
                website.save()
            else:
                if status:
                    website.status = status
                    website.save()

            return JsonResponse({'address': website.address, 'status': website.status})

        return JsonResponse({"xato": "Noto'g'ri so'rov usuli"}, status=400)


class WebsiteListView(APIView):
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request):
        with tracer.start_as_current_span("list_site_operation"):
            websites = Website.objects.all()
            serializer = WebsiteSerializer(websites, many=True)
            return Response(serializer.data)
