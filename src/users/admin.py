from django.contrib import admin

from users.models import User, Post


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "created_at")
    search_fields = ("username", "email")
    list_filter = ("created_at",)
    ordering = ("-created_at",)


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ("title", "author", "created_at")
    search_fields = ("title", "author__username")
    list_filter = ("created_at",)
    ordering = ("-created_at",)
