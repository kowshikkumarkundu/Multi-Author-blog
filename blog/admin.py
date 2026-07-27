from django.contrib import admin
from .models import Category, Tag, Post


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    search_fields = (
        "name",
    )

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    list_display = (
        "name",
        "slug",
    )

    prepopulated_fields = {
        "slug": ("name",)
    }

    search_fields = (
        "name",
    )

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

    list_display = (
        "title",
        "author",
        "category",
        "status",
        "view_count",
        "created_at",
    )

    list_filter = (
        "status",
        "category",
        "created_at",
    )

    search_fields = (
        "title",
        "content",
        "author__username",
    )

    list_select_related = (
        "author",
        "category",
    )

    autocomplete_fields = (
        "author",
        "category",
    )

    filter_horizontal = (
        "tags",
    )

    prepopulated_fields = {
        "slug": ("title",)
    }

    date_hierarchy = "created_at"

    ordering = (
        "-created_at",
    )