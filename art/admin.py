from django.contrib import admin
from .models import Art, Comment, Media, Newsletter

admin.site.register(Art)
admin.site.register(Comment)
admin.site.register(Media)
admin.site.register(Newsletter)
