# Generated by Django 2.2 on 2021-02-03 20:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0024_auto_20210203_1330'),
    ]

    operations = [
        migrations.AlterField(
            model_name='uploadfiles',
            name='feed',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Post'),
        ),
    ]