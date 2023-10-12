from django.urls import path
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    # 예: 메인 페이지를 연결하는 경우
    path('', views.index, name='index'),

	path('images/', views.images, name='images'),
    path('videos/', views.videos, name='videos'),
    # path('bulk-upload-photo/', views.bulk_upload_photo, name='bulk_upload_photo'),
    # path('bulk-upload-video/', views.bulk_upload_video, name='bulk_upload_video'),
    path('delete-selected-photos/', views.delete_selected_photos, name='delete_selected_photos')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)