from django.contrib import admin
from django.urls import path, include
from core.views import Produtos

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('api-auth/', include('rest_framework.urls')),
    path('api/', include('core.urls')),
]
