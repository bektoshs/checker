from rest_framework import serializers
from .models import Website, WebsiteWithIndex


class WebsiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Website
        fields = '__all__'


class WebsiteVersion2Serializer(serializers.ModelSerializer):
    class Meta:
        model = WebsiteWithIndex
        fields = '__all__'
