from django.contrib import admin
from .models import Announcement, Photo

@admin.register(Announcement)
class AnnouncementAdmin(admin.ModelAdmin):
    list_display = ('title', 'type', 'status', 'owner', 'created_at')
    list_filter = ('type', 'status', 'owner')
    search_fields = ('title', 'description')

@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ('id', 'announcement', 'uploaded_at')