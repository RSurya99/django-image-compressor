# Generated by Django 2.2.12 on 2021-05-07 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compressor', '0026_auto_20210507_1113'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecompressor',
            name='image_name',
            field=models.CharField(default='qGoQIzrUjC', max_length=225),
        ),
    ]
