from django.contrib import admin

from .models import Sponsor, Hacker


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
    )


@admin.register(Hacker)
class HackerAdmin(admin.ModelAdmin):

    list_display = (
        'id', 
        'name', 
        'email', 
        'message',
    )

    search_fields = (
        'name', 
        'email', 
    )

    list_filter = (
        'created',
    )
