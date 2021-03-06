# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import ShortLink, ShortLinkInfo


class ShortLinkListSerializer(serializers.HyperlinkedModelSerializer):
    """Список линков"""

    redirect_url = serializers.HyperlinkedIdentityField(
        view_name='link_redirect',
        lookup_field='short_url',
        read_only=True
    )
    detail_url = serializers.HyperlinkedIdentityField(
        view_name='link-detail',
        read_only=True
    )

    class Meta:
        model = ShortLink
        fields = ("url_target", "short_url", "redirect_url", "detail_url")

    def create(self, validated_data):
        return ShortLink.objects.create(**validated_data)


class ShortLinkInfoSerializer(serializers.ModelSerializer):

    class Meta:
        model = ShortLinkInfo
        fields = ("redirect_count", )


class ShortLinkDetailSerializer(serializers.ModelSerializer):
    """Информация об линке"""

    info = ShortLinkInfoSerializer()
    owner = serializers.SlugRelatedField(
        slug_field="username",
        read_only=True
    )

    class Meta:
        model = ShortLink
        fields = (
            "id",
            "url_target",
            "short_url",
            "owner",
            "guest",
            "info",
        )
