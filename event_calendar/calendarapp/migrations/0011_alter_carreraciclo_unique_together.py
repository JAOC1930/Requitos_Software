# Generated by Django 4.2.2 on 2023-07-23 00:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0010_materia_ciclo'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='carreraciclo',
            unique_together={('carrera', 'ciclo')},
        ),
    ]