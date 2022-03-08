from django.contrib import admin

from app.internal.models.hub import Hub


@admin.register(Hub)
class HubAdmin(admin.ModelAdmin):
    pass
