
from django.contrib import admin
from .models import VideoGame

@admin.register(VideoGame)
class VideoGameAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'genre', 'release_year')  # Show these columns in admin list
    search_fields = ('title', 'genre')                       # Enable search by title and genre
    list_filter = ('genre',)                                 # Filter by genre
