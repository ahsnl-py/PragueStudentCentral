# Generated by Django 2.2 on 2021-01-30 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0008_auto_20210130_0041'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notif_user',
            name='user_email',
            field=models.EmailField(default=0, max_length=100, unique=True),
            preserve_default=False,
        ),
    ]