# Generated by Django 2.2 on 2021-02-03 20:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0022_auto_20210203_1323'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadfiles',
            old_name='file',
            new_name='uploaded_file',
        ),
    ]
