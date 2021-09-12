# from django.shortcuts import render

# from rest_framework import generics

from django.contrib.auth.models import User

from rest_framework.generics import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView

from rest_framework.permissions import IsAuthenticated

from .models import ShortLink
from .serializers import ShortLinksSerializer

from .service import get_client_ip, base63_encode


# from rest_framework.response import Response
# from rest_framework.views import APIView


class ShortLinkView(CreateAPIView, ListAPIView):
    # permission_classes = (IsAuthenticated,)
    queryset = ShortLink.objects.filter(deleted=False)
    serializer_class = ShortLinksSerializer

    def perform_create(self, serializer):

        print()
        print(self.request.user)
        print(self.request.user.is_authenticated)
        print(self.request.data.get('owner_id'))
        print()

        if self.request.user and self.request.user.is_authenticated:
            return serializer.save(
                short_url=base63_encode(ShortLink.objects.count() + 1),
                owner = get_object_or_404(User, username=self.request.user)
            )
        else:
            return serializer.save(
                short_url=base63_encode(ShortLink.objects.count() + 1),
                guest = get_client_ip(self.request)
            )

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
