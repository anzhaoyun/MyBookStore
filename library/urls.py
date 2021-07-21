from django.contrib import admin
from django.urls import path
from library import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('add_library/',views.add_library)
]