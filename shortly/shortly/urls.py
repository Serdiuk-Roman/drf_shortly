from django.contrib import admin
from django.urls import path, include

from rest_framework.authtoken import views as drf_views

from shortly_app.views import short_link_redirect


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('shortly_app.urls')),
    path(
        'redirect/<str:short_url>/',
        short_link_redirect,
        name='link_redirect'
    ),
    # path('api-auth/', include('rest_framework.urls')),
    path('api-token-auth/', drf_views.obtain_auth_token),
]
