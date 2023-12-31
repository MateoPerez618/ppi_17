# Generated by Django 4.1.12 on 2023-10-23 05:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0003_alter_usuario_rol'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuario',
            name='privacidad',
            field=models.BooleanField(default=False, verbose_name='Acepta politicas de privacidad'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='Correo Electronico'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nacimiento',
            field=models.DateField(verbose_name='Fecha de Nacimiento'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='username',
            field=models.CharField(max_length=100, unique=True, verbose_name='Nombre de usuario'),
        ),
    ]
