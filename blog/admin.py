from django.contrib import admin

from .models import *


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("name", "body", "post", "created_on", "active")
    list_filter = ("active", "created_on")
    search_fields = ("name", "body")
    actions = ["approve_comments"]

    def approve_comments(self, request, queryset):
        queryset.update(active=True)


@admin.register(UserRate)
class RateAdmin(admin.ModelAdmin):
    list_display = ("user", "post", "rating")
    list_filter = ("user", "post")
    search_fields = ("user", "post")


@admin.register(Post)
class RateAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "date_pub", "post_views", "rating")
    search_fields = ("title", "body")
