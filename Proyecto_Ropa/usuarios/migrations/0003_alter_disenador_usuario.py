# Generated by Django 5.1.3 on 2025-01-05 10:16

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0002_remove_disenador_nombre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disenador',
            name='usuario',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='usuarios.cuenta'),
        ),
    ]
