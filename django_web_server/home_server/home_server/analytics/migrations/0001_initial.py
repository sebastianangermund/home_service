# Generated by Django 2.1.7 on 2019-04-08 14:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('things', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='LedLightData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('state_data', models.FileField(blank=True, upload_to='data_files/ledlights/')),
                ('active', models.BooleanField(default=False)),
                ('led_light', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='ledlightdata', to='things.LedLight')),
            ],
        ),
    ]