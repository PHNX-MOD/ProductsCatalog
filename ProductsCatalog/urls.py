from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('products.urls')),
    url(r'^', include('products.urls')),
    url(r'^api-auth/',include('rest_framework.urls', namespace='rest_framework')),
]
