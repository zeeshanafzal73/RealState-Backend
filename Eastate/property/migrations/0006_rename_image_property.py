# Generated by Django 4.2.4 on 2023-09-24 20:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0005_image_description_image_location_image_type'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Image',
            new_name='Property',
        ),
    ]