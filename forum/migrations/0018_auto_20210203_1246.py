# Generated by Django 2.2 on 2021-02-03 19:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0017_remove_post_upload'),
    ]

    operations = [
        migrations.RenameField(
            model_name='uploadfiles',
            old_name='file',
            new_name='files',
        ),
    ]