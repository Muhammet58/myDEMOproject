from django.contrib import admin
from .models import Blogs,Category
from django.utils.safestring import mark_safe

class BlogsAdmin(admin.ModelAdmin):
    list_display = ("title", "is_active", "is_home", "is_blog", "slug", 'selected_category',)
    list_editable = ("is_active", "is_home", "is_blog",)
    list_filter = ("is_active", "is_home", "is_blog", "categories",)
    search_fields = ("title", "description",)
    readonly_fields = ("slug",)

    def selected_category(self, obj):
        html = "<ul>"

        for category in obj.categories.all():
            html += '<li>' + category.name + '</li>'

        html += "</ul>"
        return mark_safe(html.title())

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "slug",)
    search_fields = ("name", "slug",)
    readonly_fields = ("slug",)

admin.site.register(Blogs, BlogsAdmin)
admin.site.register(Category, CategoryAdmin)