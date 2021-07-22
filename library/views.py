from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from library.models import Library
from library.serializers import LibrarySerializer
import django_filters
# Create your views here.

def add_library(request):
    data = request.POST
    serializer = LibrarySerializer(data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return JsonResponse(data,safe=False)

def get_library(request):
    librarys = Library.objects.all()
    library= LibrarySerializer(instance=librarys,many=True)
    library_list = library.data
    return JsonResponse(library_list,safe=False)

def update_library(request):
    library = Library.objects.get(id=request.POST['id'])
    data = request.POST
    serializer = LibrarySerializer(instance=library,data=data)
    serializer.is_valid(raise_exception=True)
    serializer.save()
    return JsonResponse(library)

def del_library(request):

    pass