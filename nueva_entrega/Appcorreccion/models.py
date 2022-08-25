from django.db import models


class Coberturasalud(models.Model):
    denominacion=models.CharField(max_length=60)
    codigo=models.IntegerField()
    fecha_afiliacion=models.DateField()
    

class familia(models.Model):
    nombre=models.CharField(max_length=60)
    apellido=models.CharField(max_length=60)
    dni=models.FloatField()
    extranjero=models.BooleanField()
    enfermedadbase=models.CharField(max_length=20)
    mail=models.EmailField()


class trabajo(models.Model):
    empresa=models.CharField(max_length=60)
    antiguedad= models.IntegerField()
    profesion=models.CharField(max_length=50)
    contrato=models.CharField(max_length=60)