# Generated by Django 4.0.3 on 2022-04-05 17:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('section', '0002_section_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='section',
            name='image',
        ),
    ]
