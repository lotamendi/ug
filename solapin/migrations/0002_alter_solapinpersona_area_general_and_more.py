# Generated by Django 4.1.4 on 2023-03-28 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('solapin', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='solapinpersona',
            name='area_general',
            field=models.CharField(max_length=255, verbose_name='Área general'),
        ),
        migrations.AlterField(
            model_name='solapinpersona',
            name='area_trabajo',
            field=models.CharField(max_length=255, verbose_name='Área de trabajo'),
        ),
        migrations.AlterField(
            model_name='solapinpersona',
            name='diseno_superior',
            field=models.BooleanField(default=False, verbose_name='Diseño superior (Solo para Rectoría y Vicerrectoría)'),
        ),
        migrations.AlterField(
            model_name='solapinpersona',
            name='nombre',
            field=models.CharField(max_length=255, verbose_name='Nombre y apellidos'),
        ),
    ]
