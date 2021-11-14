# Generated by Django 3.2.9 on 2021-11-14 11:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('card', '0001_initial'),
        ('association', '0001_initial'),
        ('organization', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='paircode',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='card.card'),
        ),
        migrations.AddField(
            model_name='paircode',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='created_paircode', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cardorganizationassociation',
            name='card',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='access_card', to='card.card'),
        ),
        migrations.AddField(
            model_name='cardorganizationassociation',
            name='created_by',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.SET_DEFAULT, related_name='created_cardorganizationassociation', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cardorganizationassociation',
            name='organization',
            field=models.ForeignKey(default=None, null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='associated_organization', to='organization.organization'),
        ),
        migrations.AlterUniqueTogether(
            name='cardorganizationassociation',
            unique_together={('card', 'organization')},
        ),
    ]
