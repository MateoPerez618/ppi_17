# Generated by Django 4.1.12 on 2023-10-23 01:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Role',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('nombres', models.CharField(blank=True, max_length=200, verbose_name='Nombres')),
                ('apellidos', models.CharField(blank=True, max_length=200, verbose_name='Apellidos')),
                ('nacimiento', models.DateField(default='2000-01-01', verbose_name='Fecha de Nacimiento')),
                ('direccion', models.CharField(blank=True, max_length=200, verbose_name='Direccion')),
                ('usuario_administrador', models.BooleanField(default=False)),
                ('foto_usuario', models.ImageField(blank=True, upload_to='user_photos/perfil/', verbose_name='Foto de Usuario')),
                ('foto_carnet', models.ImageField(blank=True, upload_to='user_photos/carnet/', verbose_name='Foto de Carnet')),
                ('foto_licencia_conducir', models.ImageField(blank=True, upload_to='user_photos/licencia/', verbose_name='Foto de Licencia de Conducir')),
                ('rol', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='usuarios.role', verbose_name='Rol')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
