# Generated by Django 2.0.3 on 2018-04-03 03:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_auto_20180403_1135'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='signup_type',
            field=models.CharField(choices=[('f', 'facebook'), ('e', 'email')], default='e', max_length=1),
        ),
    ]
