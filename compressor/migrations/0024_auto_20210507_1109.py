# Generated by Django 2.2.12 on 2021-05-07 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compressor', '0023_auto_20210507_1107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecompressor',
            name='image_name',
            field=models.CharField(default='LWzpZRXbVL', max_length=225),
        ),
    ]