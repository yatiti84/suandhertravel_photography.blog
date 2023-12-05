from django.contrib import admin
from blog.models import Profile, Tag, Category, Post, Photo
# Register your models here.


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    model = Profile


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    model = Tag


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    model = Category

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    model = Photo

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    model = Post
    list_display = ("id",
                    "title",
                    "subtitle",
                    "slug",
                    "publish_date",
                    "published",
                    "date_created",
                    "date_modified")

    list_filter = (
        "published",
        "publish_date",
        "tags",
        "categories",)

    list_editable = (
        "title",
        "subtitle",
        "slug",
        "publish_date",
        "published",
    )

    search_fields = (
        "title",
        "subtitle",
        "slug",
        "body",
    )
    prepopulated_fields = {
        "slug": (
            "title",
            "subtitle",
        )
    }

    date_hierarchy = "publish_date"
    save_on_top = True
