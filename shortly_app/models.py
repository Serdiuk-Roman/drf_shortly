from django.contrib.auth.models import User
from django.db import models


class ShortLink(models.Model):
    short_url = models.CharField(max_length=6, unique=True, editable=False)
    url_target = models.URLField(max_length=250, unique=True)
    owner = models.ForeignKey(
        User,
        related_name='short_links',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    guest = models.CharField(max_length=32, blank=True, null=True)
    deleted = models.BooleanField(default=False)


class ShortLinkInfo(models.Model):
    link = models.OneToOneField(
        ShortLink,
        on_delete=models.CASCADE,
        related_name='info')
    redirect_count = models.PositiveSmallIntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)
