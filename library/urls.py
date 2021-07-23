from django.contrib import admin
from django.urls import path
from library import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.get_library),
    path('add_library/',views.add_library),
    path('upd_library/',views.update_library),
    path('del_library/',views.del_library),
]