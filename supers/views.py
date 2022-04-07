from django.shortcuts import get_object_or_404, render
from supers.models import Supers
from rest_framework.decorators import api_view
from rest_framework.response import Response
from supers.serializers import SupersSerializer
from rest_framework import status

# Create your views here.


@api_view(['GET', 'POST'])
def supers_list(request):

    if request.method == 'GET':
        supers = Supers.objects.all()
        serializer = SupersSerializer(supers, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = SupersSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def supers_detail(request, pk):
    super = get_object_or_404(Supers, pk=pk)
    if request.method == 'GET':
        serializer = SupersSerializer(super)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SupersSerializer(super, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        super.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
