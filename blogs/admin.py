from django.contrib import admin
from .models import Post

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_at', 'update_at')  # Corregido: created_at
    search_fields = ('title', 'body', 'author__username')  # Corregido: author__username
    list_filter = ('created_at', 'author')  # Corregido: created_at
    ordering = ('-created_at',)  # Corregido: añadida coma para hacer tupla

admin.site.register(Post, PostAdmin)