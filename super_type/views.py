from re import S
from django.shortcuts import render
from rest_framework.decorators import api_view
from supers.models import SuperType

import super_type

# Create your views here.


@api_view(['GET'])
def super_type_list(request):
    super_type_param = request.query_params.get('heroes')

    super_type = SuperType.objects.all()
