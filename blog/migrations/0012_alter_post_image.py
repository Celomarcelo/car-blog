# Generated by Django 5.0.7 on 2024-12-10 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, default='static/images/no-image-default.jpg', null=True, upload_to='post_images/'),
        ),
    ]
