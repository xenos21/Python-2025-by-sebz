from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(Platform)
class PlatformAdmin(admin.ModelAdmin):
    list_display = ('name', 'manufacturer', 'release_year')
    search_fields = ('name', 'manufacturer')
    list_filter = ('manufacturer',)


@admin.register(Developer)
class DeveloperAdmin(admin.ModelAdmin):
    list_display = ('name', 'founded_year', 'country')
    search_fields = ('name', 'country')
    list_filter = ('country',)


@admin.register(VideoGame)
class VideoGameAdmin(admin.ModelAdmin):
    list_display = ('title', 'release_date', 'genre', 'developer', 'rating')
    search_fields = ('title',)
    list_filter = ('genre', 'developer', 'platforms')
    filter_horizontal = ('platforms',)


admin.site.register(Post)
