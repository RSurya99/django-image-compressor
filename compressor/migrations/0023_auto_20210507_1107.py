# Generated by Django 2.2.12 on 2021-05-07 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compressor', '0022_auto_20210507_1105'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecompressor',
            name='image_name',
            field=models.CharField(default='eGEFkVeQTw', max_length=225),
        ),
    ]
