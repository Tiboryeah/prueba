# Generated by Django 5.1.3 on 2025-01-06 03:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0013_remove_tipoprenda_descripcion_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tipoprenda',
            name='descripcion',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='tipoprenda',
            name='nombre',
            field=models.CharField(max_length=50, unique=True),
        ),
    ]
