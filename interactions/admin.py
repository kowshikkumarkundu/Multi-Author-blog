from django.contrib import admin
from .models import Comment, Like, Follow

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "post",
        "created_at",
    )

    search_fields = (
        "user__username",
        "post__title",
        "comment",
    )

    autocomplete_fields = (
        "user",
        "post",
    )

    ordering = (
        "-created_at",
    )

@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):

    list_display = (
        "user",
        "post",
        "created_at",
    )

    autocomplete_fields = (
        "user",
        "post",
    )

@admin.register(Follow)
class FollowAdmin(admin.ModelAdmin):

    list_display = (
        "follower",
        "following",
        "created_at",
    )

    autocomplete_fields = (
        "follower",
        "following",
    )