# Generated by Django 4.2.2 on 2023-07-22 00:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0009_carrera_ciclo_materia_carreraciclo_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='materia',
            name='ciclo',
            field=models.ForeignKey(default=0, on_delete=django.db.models.deletion.CASCADE, related_name='materia_ciclo', to='calendarapp.ciclo'),
            preserve_default=False,
        ),
    ]
