# Generated by Django 2.2 on 2021-01-30 05:30

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0003_post_subject_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='user_notif',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
