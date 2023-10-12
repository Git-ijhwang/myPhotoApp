from django.contrib import admin, messages
from django.shortcuts import render, redirect
from django.urls import path
from .models import Photo, Video
from . import views
from .forms import BulkUploadForm


@admin.register(Video)
class VideoAdmin(admin.ModelAdmin):
    list_display = ['title', 'video_file', 'date_taken']  # Admin 목록에 표시할 필드들
    search_fields = ['title', ]  # 검색할 수 있는 필드들

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            # path('bulk-upload/', views.bulk_upload, name='bulk_upload'),
            path('bulk-upload-video/', self.admin_site.admin_view(
                views.bulk_upload_video), name='bulk_upload_video'),
        ]
        return custom_urls + urls


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'date_taken']  # Admin 목록에 표시할 필드들
    search_fields = ['title', ]  # 검색할 수 있는 필드들

    def get_urls(self):
        from django.urls import path
        urls = super().get_urls()
        custom_urls = [
            # path('bulk-upload/', views.bulk_upload, name='bulk_upload'),
            path('bulk-upload-photo/', self.admin_site.admin_view(
                views.bulk_upload_photo), name='bulk_upload_photo'),
        ]
        return custom_urls + urls
