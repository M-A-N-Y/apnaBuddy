# Generated by Django 3.1.4 on 2020-12-06 23:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('committee', '0003_auto_20201206_2258'),
    ]

    operations = [
        migrations.AddField(
            model_name='events',
            name='desc',
            field=models.TextField(default='', max_length=2000),
        ),
    ]