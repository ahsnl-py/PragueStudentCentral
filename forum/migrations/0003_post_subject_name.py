# Generated by Django 2.2 on 2021-01-24 09:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forum', '0002_department_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='subject_name',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='forum.Subject'),
        ),
    ]
