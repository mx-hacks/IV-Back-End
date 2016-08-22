from django.contrib import admin

from .models import Sponsor


@admin.register(Sponsor)
class SponsorAdmin(admin.ModelAdmin):

    list_display = (
        'id', 
        'first_name', 
        'last_name', 
        'email', 
        'company',
        'message',
    )

    search_fields = (
        'first_name', 
        'last_name', 
        'email', 
        'company',
    )

    list_filter = (
        'created',
        'modified',
    )
