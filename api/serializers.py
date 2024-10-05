from rest_framework import serializers
 
# import model from models.py
from .models import APIModel
 
# Create a model serializer
class APISerializer(serializers.HyperlinkedModelSerializer):
    # specify model and fields
    class Meta:
        model = APIModel
        fields = ('title', 'description')
