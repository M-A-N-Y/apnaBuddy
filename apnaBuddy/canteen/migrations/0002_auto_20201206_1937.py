# Generated by Django 3.1.4 on 2020-12-06 14:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('canteen', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='menu',
            name='pic',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]
