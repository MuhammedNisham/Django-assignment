from django.contrib import admin
from .models import Author
from .models import Post

# Register your models here.
admin.site.register(Author)
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'author_username', 'updated_at', 'created_at')
    list_filter = ('author',)
    search_fields = ('title', 'content')
    ordering = ('-updated_at',)

    def author_username(self, obj):
        return obj.author.username
    author_username.short_description = 'AUTHOR USERNAME'

