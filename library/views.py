from django.shortcuts import render,HttpResponse
from library import models
# Create your views here.

def add_library(request):
    data = request.POST
    print(data)
    # library = models.Library(name='图书馆2',address='北京',e_mail='2014243078@qq.com',
    #     tel_number='13569830431',img='https://tse1-mm.cn.bing.net/th?id=OIP-C.dPt_kwI23ck0zG3TquTZJAHaFj&w=203&h=160&c=8&rs=1&qlt=90&o=6&dpr=1.25&pid=3.1&rm=2')
    # library.save()
    return HttpResponse("<p>添加成功！</p>")

def get_library(request):

    pass

def update_library(request):

    pass

def del_library(request):

    pass