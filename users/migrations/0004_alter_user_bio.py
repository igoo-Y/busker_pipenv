# Generated by Django 3.2.5 on 2021-08-05 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_user_login_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='bio',
            field=models.TextField(blank=True, default='소개를 입력해주세요!', null=True),
        ),
    ]