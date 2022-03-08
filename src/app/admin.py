from django.contrib import admin

from app.internal.admin.admin_user import AdminUserAdmin
from app.internal.admin.hub import HubAdmin
from app.internal.admin.publication import Publication

admin.site.site_title = "Hubs parser"
admin.site.site_header = "Hubs parser"
