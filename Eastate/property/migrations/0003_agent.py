# Generated by Django 4.2.4 on 2023-09-18 20:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0002_about'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imageSrc', models.ImageField(upload_to='media/static/images/')),
                ('title', models.CharField(max_length=250)),
                ('description', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=250)),
            ],
        ),
    ]