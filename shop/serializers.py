from rest_framework import serializers
from .models import Item

class listSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['id', 'name', 'category', 'brandName', 'image']

class itemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = ['name', 'category', 'brandName', 'image']
