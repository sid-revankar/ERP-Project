# Generated by Django 4.0.4 on 2022-07-18 05:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0012_alter_timetable_semester'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sem1attendance',
            name='status',
            field=models.BooleanField(default=True),
        ),
    ]
