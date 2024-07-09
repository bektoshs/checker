from django.urls import path
from .views import check_website, WebsiteListView

urlpatterns = [
    path('check/', check_website, name='check_website'),
    path('websites/', WebsiteListView.as_view(), name='websites_list'),
]
