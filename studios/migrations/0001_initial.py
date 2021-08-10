# Generated by Django 3.2.5 on 2021-08-10 13:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0004_alter_user_bio'),
        ('core', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('name', models.CharField(max_length=40)),
            ],
            bases=('core.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Studio',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, to='core.timestampedmodel')),
                ('name', models.CharField(blank=True, max_length=160, null=True)),
                ('desc', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(blank=True, null=True, upload_to='studio_images')),
                ('host', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='users.user')),
            ],
            bases=('core.timestampedmodel',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('timestampedmodel_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='core.timestampedmodel')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('body', models.TextField(blank=True, null=True)),
                ('category_field', models.CharField(max_length=40, null=True)),
                ('studio_field', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='studios.studio')),
                ('writer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            bases=('core.timestampedmodel',),
        ),
    ]
