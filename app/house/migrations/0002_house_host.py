# Generated by Django 2.0.3 on 2018-04-09 22:56

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('house', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='house',
            name='host',
            field=models.ForeignKey(help_text='숙소를 등록하는 호스트입니다.', on_delete=django.db.models.deletion.CASCADE, related_name='houses_with_host', to=settings.AUTH_USER_MODEL, verbose_name='호스트'),
        ),
    ]
