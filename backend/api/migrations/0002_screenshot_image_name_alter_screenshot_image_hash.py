# Generated by Django 5.0.3 on 2024-04-11 23:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='screenshot',
            name='image_name',
            field=models.CharField(default='image_name'),
        ),
        migrations.AlterField(
            model_name='screenshot',
            name='image_hash',
            field=models.CharField(max_length=255, unique=True),
        ),
    ]