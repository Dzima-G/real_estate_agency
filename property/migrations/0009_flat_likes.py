# Generated by Django 2.2.24 on 2023-09-07 17:40

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0008_complaint'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='likes',
            field=models.ManyToManyField(blank=True, related_name='flats_likes', to=settings.AUTH_USER_MODEL, verbose_name='Кто лайкнул'),
        ),
    ]
