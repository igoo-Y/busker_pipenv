# Generated by Django 3.2.5 on 2021-08-13 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0011_alter_user_busker'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='busker',
            field=models.BooleanField(null=True),
        ),
    ]
