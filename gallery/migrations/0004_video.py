# Generated by Django 4.2.2 on 2023-10-02 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gallery', '0003_photo_date_taken'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('video_file', models.ImageField(upload_to='video/')),
                ('date_taken', models.DateField(blank=True, null=True)),
            ],
        ),
    ]
