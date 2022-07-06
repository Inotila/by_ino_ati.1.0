from django.contrib import admin
from .models import Art, Comment, Newsletter


class ArtAdmin(admin.ModelAdmin):
    """this edits what the site owner can see in the admin site"""
    list_display = (
        'title',
        'date_completed',
        'price',
        'is_available',
        'media',
        'is_framed',
    )
    ordering = ('date_completed',)


admin.site.register(Art, ArtAdmin)
admin.site.register(Comment)
admin.site.register(Newsletter)
