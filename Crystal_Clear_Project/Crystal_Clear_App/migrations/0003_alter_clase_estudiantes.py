# Generated by Django 3.2.8 on 2021-10-28 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Crystal_Clear_App', '0002_alter_clase_examenes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clase',
            name='estudiantes',
            field=models.ManyToManyField(blank=True, to='Crystal_Clear_App.Estudiante'),
        ),
    ]
