# Generated by Django 3.2.13 on 2022-06-04 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospitalApp', '0003_auto_20220604_2120'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pacientes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Nombres', models.CharField(max_length=50)),
                ('Apellidos', models.CharField(max_length=50)),
                ('Dni', models.CharField(max_length=30)),
                ('Direccion', models.CharField(max_length=100)),
                ('Telefono', models.CharField(max_length=20)),
                ('sexo', models.CharField(max_length=20)),
                ('FechaNacimiento', models.DateField()),
                ('FechaResgistro', models.DateField(auto_now_add=True)),
                ('FechaModificacion', models.DateField(auto_now_add=True)),
                ('UsuarioRegistro', models.CharField(max_length=50)),
                ('UsuarioModificacion', models.CharField(max_length=50)),
                ('Activo', models.BooleanField(default=True)),
            ],
        ),
    ]
