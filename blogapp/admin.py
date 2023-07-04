from django.contrib import admin
from .models import Blogs,Category

class BlogsAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "is_home", "is_blog", "slug",)
    list_editable = ("is_active", "is_home", "is_blog",)
    list_filter = ("category", "is_active", "is_home", "is_blog")
    search_fields = ("title", "description",)
    readonly_fields = ("slug",)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)
    search_fields = ("name", "slug",)
    readonly_fields = ("slug",)

admin.site.register(Blogs, BlogsAdmin)
admin.site.register(Category, CategoryAdmin)