from django.db import models


class ShortLink(models.Model):
    short_url = models.CharField(max_length=6, unique=True, editable=False)
    url_target = models.URLField(max_length=250, unique=True)
    owner = models.ForeignKey(
        'auth.User',
        related_name='shortlies',
        on_delete=models.DO_NOTHING,
        blank=True,
        null=True
    )
    guest = models.CharField(max_length=32, blank=True, null=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        verbose_name = 'Short_Url'
        verbose_name_plural = 'Short_Urls'


class ShortLinkInfo(models.Model):
    link = models.OneToOneField(
        ShortLink,
        on_delete=models.CASCADE,
        related_name='info')
    guest = models.CharField(max_length=32, blank=True, null=True)
    last_datetime = models.DateTimeField(auto_now=True)
    click_count = models.PositiveSmallIntegerField(default=0)
