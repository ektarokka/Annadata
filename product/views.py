from django.shortcuts import render
from django.http import HttpResponse 
from django.http import JsonResponse 
from rest_framework.decorators import api_view
from rest_framework.response import Response
from . serializers import CategorySerializer
from . models import Category
# Create your views here.
@api_view(['GET'])
def Categoryview(request):
    api_urls = {
        'List':'/task-list/',
        'Detail-view':'/task-detail/<str:pk>/',
        'Create':'/task-create/',
        'Update':'/task-update/<str:pk>/',
        'Delete':'/task-delete/<str:pk>/',

    }
    return Response(api_urls)
@api_view(['GET'])
def CategoryListview(request):
    cat = Category.objects.all()
    serializer= CategorySerializer(cat,many=True)
    return Response(serializer.data)
    
