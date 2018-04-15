# Generated by Django 2.0.3 on 2018-04-15 12:05

from django.db import migrations
import imagekit.models.fields
import members.models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20180414_2119'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofileimages',
            name='img_profile_225',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='', upload_to=members.models.dynamic_img_profile_path),
        ),
        migrations.AddField(
            model_name='userprofileimages',
            name='img_profile_28',
            field=imagekit.models.fields.ProcessedImageField(blank=True, default='', upload_to=members.models.dynamic_img_profile_path),
        ),
    ]
