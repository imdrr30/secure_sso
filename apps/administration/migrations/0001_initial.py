# Generated by Django 3.2.9 on 2021-11-10 17:08

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UserType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('identity', models.CharField(max_length=512, verbose_name='Name/Title')),
                ('description', models.TextField(blank=True, default=None, null=True)),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
    ]