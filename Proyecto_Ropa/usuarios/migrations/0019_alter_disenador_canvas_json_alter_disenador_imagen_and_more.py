# Generated by Django 5.1.3 on 2025-01-06 07:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0018_disenador_canvas_json'),
    ]

    operations = [
        migrations.AlterField(
            model_name='disenador',
            name='canvas_json',
            field=models.JSONField(),
        ),
        migrations.AlterField(
            model_name='disenador',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='disenos/'),
        ),
        migrations.AlterField(
            model_name='disenador',
            name='tipo_prenda',
            field=models.CharField(max_length=50),
        ),
    ]
