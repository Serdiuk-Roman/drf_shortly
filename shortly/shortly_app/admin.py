from django.contrib import admin

from .models import ShortLink, ShortLinkInfo


admin.site.register(ShortLink)
admin.site.register(ShortLinkInfo)