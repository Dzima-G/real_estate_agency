# Generated by Django 2.2.24 on 2023-09-05 15:25

from django.db import migrations


def correct_value_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Flat.objects.filter(construction_year__gte=2015).update(new_building=True)
    Flat.objects.filter(construction_year__lt=2015).update(new_building=False)


class Migration(migrations.Migration):
    dependencies = [
        ('property', '0004_auto_20230902_1211'),
    ]

    operations = [
        migrations.RunPython(correct_value_building)
    ]
