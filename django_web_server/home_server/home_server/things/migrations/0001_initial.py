# Generated by Django 2.1.7 on 2019-03-29 11:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='LedLight',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=64)),
                ('address', models.CharField(blank=True, default='', max_length=64, null=True)),
                ('state', models.CharField(choices=[('-', 'inactive'), ('0', 'off'), ('1', 'on')], default='-', max_length=1)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ledlight', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['state', 'owner'],
            },
        ),
    ]
