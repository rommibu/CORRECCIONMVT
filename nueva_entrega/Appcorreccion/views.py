from django.http import HttpResponse
from django.shortcuts import render
from .models import Coberturasalud, familia, trabajo
import datetime

def Cobertura_salud(request):
    Cobertura=Coberturasalud(denominacion="Swiss Medical", codigo=15893, fecha_afiliacion="2015-10-28") 
    Cobertura.save()
    texto=f"Base de Coberturas de Salud familiar creado: nombre: {Cobertura.denominacion} codigo: {Cobertura.codigo}"
    return HttpResponse(texto)
    
def familia_vinculo(request):
    Familia=familia(nombre="Romina", apellido="Galeano", dni=27598874, extranjero="False", enfermedadbase="Diabetes", mail="rommibu@gmail.com")
    Familia.save()
    texto=f"Nuevo familiar agregado: nombre: {Familia.nombre} apellido: {Familia.apellido} dni: {Familia.dni} extranjero: {Familia.extranjero} enfermedadbase: {Familia.enfermedadbase} mail: {Familia.mail}"
    return HttpResponse(texto)


def trabajo_titular(request):
    Trabajo=trabajo(empresa="NaranjaX", antiguedad= 7, profesion="Analista", contrato="Temporal")
    Trabajo.save()
    texto=f"Descripcion de trabajo agregado: empresa{Trabajo.empresa} antiguedad: {Trabajo.antiguedad} profesion: {Trabajo.profesion} contrato{Trabajo.contrato}"
    return HttpResponse(texto)
