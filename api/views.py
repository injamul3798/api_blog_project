# import viewsets
from rest_framework import viewsets

# import local data
from .serializers import APISerializer
from .models import APIModel
from django.shortcuts import render

# create a viewset


class APIViewSet(viewsets.ModelViewSet):
	# define queryset
	queryset = APIModel.objects.all()

	# specify serializer to be used
	serializer_class = APISerializer
	
def api_data_view(request):
    api_data = APIModel.objects.all()
    return render(request, 'api_data.html', {'api_data': api_data})
