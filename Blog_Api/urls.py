from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls'), name='post'),
    # API AUTH
    path("api-auth/", include('rest_framework.urls'), name='rest_framework'),
]
