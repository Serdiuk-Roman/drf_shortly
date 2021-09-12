# -*- coding: utf-8 -*-

from rest_framework import serializers

from .models import ShortLink


class ShortLinksSerializer(serializers.ModelSerializer):
    """Список линков"""

    class Meta:
        model = ShortLink
        # fields = "__all__"
        exclude = ("id", "deleted")

    def create(self, validated_data):
        return ShortLink.objects.create(**validated_data)