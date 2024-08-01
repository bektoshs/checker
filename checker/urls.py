from django.urls import path
from .views import check_website, WebsiteListView, check_website_version2

urlpatterns = [
    path('check/', check_website, name='check_website'),
    path('check/v2/', check_website_version2, name='check_website'),
    path('websites/', WebsiteListView.as_view(), name='websites_list'),
]
