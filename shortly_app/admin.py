from django.contrib import admin

from .models import ShortLink, ShortLinkInfo


class ShortLinkAdmin(admin.ModelAdmin):
    readonly_fields = ('short_url',)


class ShortLinkInfoAdmin(admin.ModelAdmin):
    readonly_fields = ('redirect_count',)


admin.site.register(ShortLink, ShortLinkAdmin)
admin.site.register(ShortLinkInfo, ShortLinkInfoAdmin)
