# Generated by Django 4.2.2 on 2023-07-19 15:59

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0003_archivos_alter_event_id_alter_eventmember_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivos',
            name='fecha_subida',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]