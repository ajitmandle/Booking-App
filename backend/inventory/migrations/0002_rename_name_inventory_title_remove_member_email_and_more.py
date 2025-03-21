# Generated by Django 5.1.7 on 2025-03-17 12:50

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='inventory',
            old_name='name',
            new_name='title',
        ),
        migrations.RemoveField(
            model_name='member',
            name='email',
        ),
        migrations.AddField(
            model_name='inventory',
            name='description',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='inventory',
            name='expiration_date',
            field=models.DateField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='booking_count',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='member',
            name='date_joined',
            field=models.DateTimeField(default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='member',
            name='surname',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
    ]
