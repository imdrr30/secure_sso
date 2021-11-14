# Generated by Django 3.2.9 on 2021-11-14 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import phonenumber_field.modelfields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CardType',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('identity', models.CharField(max_length=512, verbose_name='Name/Title')),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='created_cardtype', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('is_active', models.BooleanField(default=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('card_uid', models.CharField(max_length=512, unique=True)),
                ('provided_email', models.EmailField(default=None, max_length=254, null=True)),
                ('provided_phone_number', phonenumber_field.modelfields.PhoneNumberField(default=None, max_length=128, null=True, region=None)),
                ('provided_organization_custom_data', models.JSONField(default=None, null=True)),
                ('user_id_for_organization', models.TextField(default=None, null=True)),
                ('customer_data', models.JSONField(default=None, null=True)),
                ('card_owned_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='owned_card', to=settings.AUTH_USER_MODEL)),
                ('card_type', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='card.cardtype')),
                ('created_by', models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='created_card', to=settings.AUTH_USER_MODEL)),
                ('provided_organization', models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='provider_organization', to='organization.organization')),
            ],
            options={
                'ordering': ['-created'],
                'abstract': False,
            },
        ),
    ]
