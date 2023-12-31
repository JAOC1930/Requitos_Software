# Generated by Django 4.2.2 on 2023-07-23 22:41

from django.db import migrations, models
import datetime

class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0011_alter_carreraciclo_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='asignacion',
            name='descripcion',
            field=models.CharField(default='Valor predeterminado para descripción', max_length=200),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='fecha_final',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='asignacion',
            name='fecha_inicio',
            field=models.DateTimeField(default=datetime.datetime.now),  # Cambia el valor por defecto aquí
            preserve_default=False,
        ),
    ]
