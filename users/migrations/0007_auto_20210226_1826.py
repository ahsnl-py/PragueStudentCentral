# Generated by Django 2.2 on 2021-02-27 01:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_auto_20210226_1816'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofile',
            name='user_department',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='forum.Department'),
        ),
    ]