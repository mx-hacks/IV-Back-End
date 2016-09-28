from django.contrib import admin

from .models import (
    School,
    Campus,
    Hackathon,
    EventEdition,
    Hacker,
)


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):

    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Campus)
class CampusAdmin(admin.ModelAdmin):

    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(Hackathon)
class HackathonAdmin(admin.ModelAdmin):

    list_display = ('id', 'name',)
    search_fields = ('name',)


@admin.register(EventEdition)
class EventEditionAdmin(admin.ModelAdmin):

    list_display = ('id', 'name', 'edition')
    search_fields = ('name',)


@admin.register(Hacker)
class HackerAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'email',
        'first_name',
        'last_name',
        'phone_number',
        'male',
        'female',
    )

    list_filter = (
        'first_time_hacker',
        'first_time_event',
        'male',
        'female',
        'country',
        'state',
        'age',
        'school',
        'education_level',
        'tshirt_size',
        'hackathons',
    )

    search_fields = ('email', 'first_name', 'last_name', 'phone_number')

    raw_id_fields = ('school', 'campus',)
