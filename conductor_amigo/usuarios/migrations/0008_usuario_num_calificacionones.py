# Generated by Django 4.1.12 on 2023-11-20 13:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0007_alter_usuario_calificacion_calificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='num_calificacionones',
            field=models.PositiveIntegerField(default=0),
        ),
    ]
