# Generated by Django 2.2 on 2021-02-01 05:00

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0012_auto_20210130_1224'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='upload',
            field=models.ImageField(default=django.utils.timezone.now, upload_to='static/images'),
            preserve_default=False,
        ),
    ]
