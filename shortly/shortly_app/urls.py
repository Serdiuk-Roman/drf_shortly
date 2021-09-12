from django.urls import path

from . import views


urlpatterns = [
    path('', views.ShortLinkView.as_view()),
    path('link/<int:pk>/', views.ShortLinkDetailView.as_view()),
]
