from django.contrib import admin
from django.urls import path
from library import views
from rest_framework.documentation import include_docs_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.get_library),
    path('api_doc/', include_docs_urls(title='API接口文档')),
    path('add_library/',views.add_library),
]