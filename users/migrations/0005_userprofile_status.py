# Generated by Django 2.2 on 2021-02-27 01:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0004_userprofile_user_picture'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='status',
            field=models.CharField(choices=[('student', 'Student'), ('graduate', 'Graduate'), ('future student', 'Future Student')], default='draft', max_length=10),
        ),
    ]