# Generated by Django 3.2.9 on 2021-11-10 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('card', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='card',
            name='provided_organization_custom_data',
            field=models.JSONField(default=None, null=True),
        ),
    ]
