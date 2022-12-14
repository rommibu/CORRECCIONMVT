# Generated by Django 4.1 on 2022-08-25 17:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Coberturasalud',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('denominacion', models.CharField(max_length=60)),
                ('codigo', models.IntegerField()),
                ('fecha_afiliacion', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='familia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=60)),
                ('apellido', models.CharField(max_length=60)),
                ('dni', models.FloatField()),
                ('extranjero', models.BooleanField()),
                ('enfermedadbase', models.CharField(max_length=20)),
                ('mail', models.EmailField(max_length=254)),
            ],
        ),
        migrations.CreateModel(
            name='trabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('empresa', models.CharField(max_length=60)),
                ('antiguedad', models.IntegerField()),
                ('profesion', models.CharField(max_length=50)),
                ('contrato', models.CharField(max_length=60)),
            ],
        ),
    ]
