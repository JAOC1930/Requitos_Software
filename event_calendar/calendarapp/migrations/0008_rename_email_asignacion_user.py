# Generated by Django 4.2.2 on 2023-07-20 00:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('calendarapp', '0007_rename_user_asignacion_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='asignacion',
            old_name='email',
            new_name='user',
        ),
    ]