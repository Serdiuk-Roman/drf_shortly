from django.urls import path


# from rest_framework import routers

from . import views


# router = routers.DefaultRouter()
# router.register(r'urls', URLList)

urlpatterns = [
    path('', views.ShortLinkView.as_view()),
]
