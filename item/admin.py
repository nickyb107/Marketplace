from django.contrib import admin

from .models import item, Review

class CommentInLine(admin.TabularInline):
    model = Review

class ItemAdmin(admin.ModelAdmin):
    inlines = [
        CommentInLine
    ]


admin.site.register(item)
admin.site.register(Review)
