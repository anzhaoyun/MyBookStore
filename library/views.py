from django.shortcuts import render,HttpResponse
from django.http import JsonResponse
from library.models import Library
from library.serializers import LibrarySerializer
import django_filters
# Create your views here.

def add_library(request):
    data = request.POST
    try:
        serializer = LibrarySerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
    except Exception as e:
        return JsonResponse({'errors':f"{e}"},safe=False)
    return JsonResponse(data,safe=False)

def get_library(request):
    try:
        librarys = Library.objects.all()
        library= LibrarySerializer(instance=librarys,many=True)
        library_list = library.data
        return JsonResponse(library_list,safe=False)
    except Exception as e:
        return JsonResponse({'errors':f"{e}"},safe=False)

def update_library(request):
    try:
        library = Library.objects.get(id=request.POST['id'])
        data = {'name':request.POST['name'],'address':request.POST['address']}
        serializer = LibrarySerializer(instance=library,data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        result = LibrarySerializer(instance=Library.objects.get(id=request.POST['id']))
    except Exception as e:
        return JsonResponse({'errors':f"{e}"},safe=False)
    return JsonResponse(result.data,safe=False)

def del_library(request):
    try:
        library = Library.objects.get(id=request.POST['id'])
        result = LibrarySerializer(instance=library).data
        library.delete()
    except Exception as e:
        return JsonResponse({'errors':f"{e}"},safe=False)
    return JsonResponse(result,safe=False)