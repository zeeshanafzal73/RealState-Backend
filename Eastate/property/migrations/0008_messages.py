# Generated by Django 4.2.4 on 2023-09-27 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0007_news_author_news_description_news_paragraph_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Messages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('email', models.EmailField(max_length=250)),
                ('comment', models.TextField(max_length=500)),
            ],
        ),
    ]
