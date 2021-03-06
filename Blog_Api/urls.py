from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('blog.urls'), name='post'),
    # API AUTH
    path('api-auth/', include('rest_framework.urls'), name='rest_framework'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # API REGISTER User
    path('api/users/', include('users.urls'), name='users'),
]
