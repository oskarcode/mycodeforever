# Generated by Django 3.1.2 on 2020-11-23 14:51

from django.db import migrations
import django_resized.forms


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20201031_1656'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='header_image',
            field=django_resized.forms.ResizedImageField(blank=True, crop=None, force_format=None, keep_meta=True, null=True, quality=0, size=[500, 300], upload_to='images/'),
        ),
    ]
