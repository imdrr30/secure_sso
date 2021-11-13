# Generated by Django 3.2.9 on 2021-11-13 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='organization',
            name='superadmin_email',
            field=models.EmailField(default=None, max_length=512, null=True),
        ),
        migrations.AddField(
            model_name='organization',
            name='superadmin_password',
            field=models.CharField(default=None, max_length=512, null=True),
        ),
    ]