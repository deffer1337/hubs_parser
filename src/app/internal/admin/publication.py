from django.contrib import admin

from app.internal.models.publication import Publication


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    pass
