from django.contrib import admin

from .models import Application


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):

    list_display = ('id', 'hacker', 'step', 'finished', 'accepted')
    list_editable = ('step', 'finished', 'accepted')

    list_filter = ('finished', 'step', 'accepted',)

    search_fields = (
        'hacker__email',
        'hacker__first_name',
        'hacker__last_name',
    )