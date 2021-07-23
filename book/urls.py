from django.contrib import admin
from django.urls import path
from book import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.get_book),
    path('add_library/',views.add_book),
    path('upd_library/',views.upd_book),
    path('del_library/',views.del_book),
]