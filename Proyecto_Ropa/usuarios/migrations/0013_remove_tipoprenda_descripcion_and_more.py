# Generated by Django 5.1.3 on 2025-01-06 03:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0012_tipoprenda_descripcion_alter_tipoprenda_nombre'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tipoprenda',
            name='descripcion',
        ),
        migrations.AlterField(
            model_name='tipoprenda',
            name='nombre',
            field=models.CharField(max_length=50),
        ),
    ]
