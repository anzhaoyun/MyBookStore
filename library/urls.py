
from django.urls import path
from library import views
urlpatterns = [
    path('add_library/',views.add_library)
]