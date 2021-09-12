from django.contrib.auth.models import User
from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from rest_framework.authtoken.models import Token

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
    guest = models.CharField(max_length=32, blank=True, null=True)
    last_datetime = models.DateTimeField(auto_now=True)
    click_count = models.PositiveSmallIntegerField(default=0)


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)