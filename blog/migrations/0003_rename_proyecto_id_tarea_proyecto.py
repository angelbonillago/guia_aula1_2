# Generated by Django 4.1.3 on 2022-11-28 16:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_tarea'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tarea',
            old_name='proyecto_id',
            new_name='proyecto',
        ),
    ]
