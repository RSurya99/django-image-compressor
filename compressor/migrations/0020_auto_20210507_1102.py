# Generated by Django 2.2.12 on 2021-05-07 04:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('compressor', '0019_auto_20210507_1100'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imagecompressor',
            name='image_name',
            field=models.CharField(default='uQWsSVESji', max_length=225),
        ),
    ]
