# Generated by Django 4.2.8 on 2023-12-24 22:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0002_customization_faces_in_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='customization',
            name='special_notes',
            field=models.TextField(null=True),
        ),
    ]