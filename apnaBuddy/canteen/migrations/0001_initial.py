# Generated by Django 3.1.4 on 2020-12-06 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Manager',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('phone', models.CharField(max_length=10, null=True)),
                ('balance', models.FloatField(default=0)),
                ('email', models.EmailField(max_length=254)),
                ('profile_pic', models.ImageField(null=True, upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
                ('price', models.FloatField(default=0)),
                ('pic', models.ImageField(null=True, upload_to='')),
                ('category', models.CharField(choices=[('lunch', 'lunch'), ('breakfast', 'breakfast'), ('snack', 'snack')], max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('delivered', models.BooleanField(default=False)),
                ('canteen', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='canteen.manager')),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='canteen.menu')),
            ],
        ),
    ]