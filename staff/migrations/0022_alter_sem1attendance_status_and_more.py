# Generated by Django 4.0.4 on 2022-07-18 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('staff', '0021_alter_sem1attendance_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sem1attendance',
            name='status',
            field=models.CharField(default='Present', max_length=7),
        ),
        migrations.AlterField(
            model_name='sem2attendance',
            name='status',
            field=models.CharField(default='Present', max_length=7),
        ),
        migrations.AlterField(
            model_name='sem3attendance',
            name='status',
            field=models.CharField(default='Present', max_length=7),
        ),
        migrations.AlterField(
            model_name='sem4attendance',
            name='status',
            field=models.CharField(default='Present', max_length=7),
        ),
        migrations.AlterField(
            model_name='sem5attendance',
            name='status',
            field=models.CharField(default='Present', max_length=7),
        ),
        migrations.AlterField(
            model_name='sem6attendance',
            name='status',
            field=models.CharField(default='Present', max_length=7),
        ),
    ]