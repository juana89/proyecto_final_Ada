# -*- coding: utf-8 -*-
"""proceso_cuenta.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/116Gm37K6Z5IVHHSRAoQElopeasWL9R6s
"""



#!/usr/bin/env python
# -*- coding: utf-8 -*-
# author: <Juana Regert>

"""

creacion de cuenta para cada persona , (identificacion de cuenta con el dni)

"""
import csv
from persona import Persona

def crear_cuentas():
 personas = {}
 archivo = open("personas.csv","r")
 archivo_csv = csv.reader(archivo)
 titulos= next (archivo_csv)
 for nombre, dni, fecha_nacimiento in archivo_csv:
   persona =Persona(dni, nombre, fecha_nacimiento)
   personas[dni] = persona
 archivo.close()
 return personas

def archivar_cuentas(lista_cuentas):
  lista_de_tuiplas = [('Titular' , 'saldo' , 'Nro Cuenta' , 'Activa')]
  for elemneto in lista_cuentas:
    titular =elemento.titular
    saldo = elemento.saldo
    Ncuenta = elemento.activa 
    lista_de_tuplas.append(ttitular,saldo,Ncuenta,estado)
  archivo = open ("cuentas.csv","w" ,newline= " ")
  archivo_csv = csv.write(archivo)
  archivo_csv.writerows(lista_de_tuplas)
  archivo.close()

  def procesar_gastos(cuenta,archivo):
    pass

  def procesar_deposito(cuenta,archivo):
     pass

  def procesar_transferencia(cuenta,archivo):
    pass