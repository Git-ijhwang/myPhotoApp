from django.db import models

# Create your models here.


class Photo(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='photos/', unique=True)
    date_taken = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title


class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='video/', unique=True)
    date_taken = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
