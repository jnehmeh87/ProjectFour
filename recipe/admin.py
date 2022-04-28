from django.contrib import admin
from .models import Recipe, Comments
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Recipe)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'slug', 'status', 'created_on')
    search_fields = ['title', 'preparation_content']
    prepopulated_fields = {'slug': ('title',)}
    list_filter = ('status', 'created_on')
    summernote_fields = ('ingredients', 'preparation_content')


@admin.register(Comments)
class CommentAdmin(admin.ModelAdmin):

    list_display = ('name', 'body', 'recipe', 'created_on', 'approved')
    list_filter = ('approved', 'created_on')
    search_fields = ['name', 'email', 'body']
    actions = ['approved_comments']

    def approved_comments(self, request, queryset):
        queryset.update(approved=True)
