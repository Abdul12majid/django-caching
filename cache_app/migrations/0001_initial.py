# Generated by Django 5.1 on 2024-12-02 15:13

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('serial_number', models.UUIDField(default=uuid.uuid4, editable=False)),
            ],
        ),
    ]
