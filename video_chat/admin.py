from django.contrib import admin
from .models import OpenTokSessions, OpenTokTokens

admin.site.register(OpenTokSessions)
admin.site.register(OpenTokTokens)