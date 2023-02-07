# Generated by Django 4.1.4 on 2023-01-26 11:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posgrado', '0005_posgrado'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('CI', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido1', models.CharField(max_length=50)),
                ('apellido2', models.CharField(max_length=50)),
                ('nacionalidad', models.CharField(default='Cubana', max_length=20)),
                ('pasaporte', models.CharField(blank=True, max_length=20)),
                ('sexo', models.CharField(choices=[('F', 'Femenino'), ('M', 'Masculino')], max_length=10, verbose_name='Sexo')),
                ('domicilio', models.CharField(max_length=150)),
                ('telefono', models.CharField(blank=True, max_length=20)),
                ('correo', models.EmailField(blank=True, max_length=50)),
            ],
            options={
                'verbose_name': 'persona',
                'verbose_name_plural': 'personas',
                'ordering': ['apellido1'],
            },
        ),
    ]