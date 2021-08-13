# Generated by Django 3.2.5 on 2021-08-13 12:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('broadcasts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='broadcast',
            name='image',
            field=models.ImageField(blank=True, default='img/static/img/no_image.png', null=True, upload_to='broadcast_images'),
        ),
        migrations.AlterField(
            model_name='broadcast',
            name='on_air',
            field=models.BooleanField(default=False, null=True),
        ),
    ]
