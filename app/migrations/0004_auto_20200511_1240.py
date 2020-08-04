# Generated by Django 3.0.2 on 2020-05-11 16:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_auto_20200504_1233'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estudiante',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1),
        ),
        migrations.AlterField(
            model_name='profesor',
            name='sexo',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Femenino')], max_length=1),
        ),
    ]