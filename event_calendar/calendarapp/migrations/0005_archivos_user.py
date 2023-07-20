# Generated by Django 4.2.2 on 2023-07-19 16:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('calendarapp', '0004_archivos_fecha_subida'),
    ]

    operations = [
        migrations.AddField(
            model_name='archivos',
            name='user',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, related_name='user_archivo', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
    ]
