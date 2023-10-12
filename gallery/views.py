# from django.shortcuts import render

# # Create your views here.
from django.http import HttpResponse

# def index(request):
#     return HttpResponse("Hello, this is the gallery index.")

from django.shortcuts import render
import os
import re
import shutil
import mimetypes

from django.shortcuts import render, redirect
from django.conf import settings
from django.contrib import messages
from django.templatetags.static import static
from django.core.paginator import Paginator
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from .forms import BulkUploadForm
from .models import Photo, Video
from datetime import datetime


class FoundEnoughFiles(Exception):
    pass


def copy_to_static(file_path):
    file_name = os.path.basename(file_path)

    static_file_path = '/Users/root1/Desktop/Development/Django/Django_example/mediaExploler/static/' + file_name

    if not os.path.exists(static_file_path):
        shutil.copy2(file_path, static_file_path)

    return static(file_name)

# Create your views here.


def list_files(dir, ext):
    r = []
    # try:
    for root, dirs, files in os.walk(dir):
        for file in files:
            if file.startswith('.'):
                continue
            if file.endswith(ext):
                full_path = os.path.join(root, file)
                static_path = copy_to_static(full_path)
                r.append((static_path, os.path.getmtime(full_path)))

                # if len(r)>= 10:
                #     raise FoundEnoughFiles

    # except FoundEnoughFiles:
    #     pass

    r.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in r]


def index(request):

    # image_files = list_files('/Volumes/Samsung_T5/CloudPhotoBackup', '.jpg')
    # video_files = list_files('/Volumes/Samsung_T5/CloudPhotoBackup', '.mp4')

    # paginator = Paginator(image_files, 100)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)

    # return render(request, 'explorer/index.html', {'images': page_obj, 'videos': video_files})
    return render(request, 'gallery/index.html')


def images(request):
    years = range(2013, 2025)
    year = request.GET.get('year')
    if year:
        photos = Photo.objects.filter(
            date_taken__year=year).order_by('date_taken')
    # image_files = list_files('/Volumes/Samsung_T5/CloudPhotoBackup', '.jpg')
    else:
        photos = Photo.objects.all()

    paginator = Paginator(photos, 100)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'years': years,
        'year': year
    }

    return render(request, 'gallery/images.html', context)


def videos(request):
    years = range(2013, 2025)
    # video_files = list_files('/Volumes/Samsung_T5/CloudPhotoBackup', '.mp4')
    year = request.GET.get('year')
    if year:
        video_files = Video.objects.filter(
            date_taken__year=year).order_by('date_taken')
    else:
        video_files = Video.objects.all()
        year = 0

    paginator = Paginator(video_files, 50)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        'page_obj': page_obj,
        'years': years,
        'year': year
    }

    return render(request, 'gallery/videos.html', context)


@csrf_exempt
@require_POST
def clear(request):
    file_types = ('*.jpg', '*.mp4')  # Add or remove file types as needed
    files_grabbed = []
    for file_type in file_types:
        files_grabbed.extend(
            glob.glob(os.path.join(settings.STATIC_ROOT, file_type)))
    for file in files_grabbed:
        os.remove(file)
    return JsonResponse({'status': 'success'})


def func_date_take(match):
    date_taken = None
    if match:
        year, month, day = match.groups()

        if int(year) < 2013 or int(year) > 2025:
            date_taken = None

        elif (int(month) <= 0) or (int(month) > 12):
            date_taken = None

        elif (int(day) <= 0 or int(day) > 31):
            date_taken = None

        else:
            date_taken = datetime(
                int(year), int(month), int(day)).date()

    return date_taken


def bulk_upload_photo(request):
    if request.method == 'POST':
        form = BulkUploadForm(request.POST, request.FILES)
        if form.is_valid():
            for f in request.FILES.getlist('files'):
                ext = os.path.splitext(f.name)[1].lower()

                if ext in ['.jpg', '.jpeg', '.gif']:
                    match = re.search(r'(\d{4})(\d{2})(\d{2})', f.name)
                    photo = Photo(image=f, date_taken=func_date_take(match))
                    photo.save()
                else:
                    messages.warning(request, f"{f.name} is not JPEG image")

            return redirect('admin:gallery_photo_changelist')
    else:
        form = BulkUploadForm()
    return render(request, 'gallery/admin/bulk_upload_photo.html', {'form': form})


def bulk_upload_video(request):
    if request.method == 'POST':
        form = BulkUploadForm(request.POST, request.FILES)
        if form.is_valid():
            for f in request.FILES.getlist('video'):
                ext = os.path.splitext(f.name)[1].lower()

                if ext in ['.mp4']:
                    match = re.search(r'(\d{4})(\d{2})(\d{2})', f.name)
                    video = Video(
                        video_file=f, date_taken=func_date_take(match))
                    video.save()
                else:
                    messages.warning(request, f"{f.name} is not Video files")

            return redirect('admin:gallery_video_changelist')
    else:
        form = BulkUploadForm()
    return render(request, 'gallery/admin/bulk_upload_video.html', {'form': form})

def delete_selected_photos(request):
    if request.method == "POST" :
        selected_photos = request.POST.getlist('selected_photos')

        if not selected_photos:
            return HttpResponse("No Photos selected")
        
        Photo.objects.filter(id__in=selected_photos).delete()
        return redirect('/')

    return HttpResponse("Method not allowed", status=405)