# Generated by Django 5.1.3 on 2025-01-06 02:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0009_alter_disenador_usuario'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disenador',
            name='tipo_prenda',
            field=models.CharField(max_length=100),
        ),
    ]
