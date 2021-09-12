# from django.shortcuts import render

# from rest_framework import generics

from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.shortcuts import redirect

from rest_framework.generics import get_object_or_404
from rest_framework.generics import CreateAPIView, ListAPIView
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import ShortLink, ShortLinkInfo
from .serializers import ShortLinkListSerializer, ShortLinkDetailSerializer
from .permissions import IsAuthor
from .service import get_client_ip, base63_encode

# from rest_framework.decorators import api_view
# from rest_framework.reverse import reverse


class ShortLinkView(CreateAPIView, ListAPIView):
    """Вывод списка гиперссылок"""
    queryset = ShortLink.objects.filter(deleted=False)
    serializer_class = ShortLinkListSerializer

    def perform_create(self, serializer):
        if self.request.user.is_authenticated:
            return serializer.save(
                short_url=base63_encode(ShortLink.objects.count() + 1),
                owner=get_object_or_404(User, username=self.request.user)
            )
        else:
            return serializer.save(
                short_url=base63_encode(ShortLink.objects.count() + 1),
                guest=get_client_ip(self.request)
            )


class ShortLinkDetailView(APIView):
    """Вывод информации о гиперссылке"""

    permission_classes = [IsAuthor, ]

    def get(self, request, pk):
        link = get_object_or_404(ShortLink, id=pk, deleted=False)
        self.check_object_permissions(request, link)
        serializer = ShortLinkDetailSerializer(link)
        return Response(serializer.data)

    def delete(self, request, pk):
        link = get_object_or_404(ShortLink, id=pk)
        self.check_object_permissions(request, link)
        serializer = ShortLinkDetailSerializer(
            instance=link,
            data=request.data,
            partial=True
        )
        if serializer.is_valid(raise_exception=True):
            serializer.save(deleted=True)
        return Response(status=status.HTTP_204_NO_CONTENT)


def short_link_redirect(request, short_url):
    data = get_object_or_404(ShortLink, short_url=short_url)

    try:
        info = ShortLinkInfo.objects.get(link=data)
    except ObjectDoesNotExist:
        info = ShortLinkInfo(
            link=data,
            click_count=0
        )
    info.click_count += 1
    info.save()
    return redirect(data.url_target)


# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'shortly': reverse('shortly-list', request=request, format=format)
#     })
