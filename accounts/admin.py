from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "is_author",
        "created_at",
    )

    list_filter = (
        "is_author",
    )

    search_fields = (
        "user__username",
        "user__email",
        "user__first_name",
        "user__last_name",
    )
    
    list_editable = (
        "is_author",
    )

    autocomplete_fields = (
        "user",
    )