# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 20:38:34 2022

@author: Manuel
"""
#Damos acceso a las funciones matematicas
import math
#Imprimimos los mensajes de bienvenida y la decision de quiere pasar de decimal a grados o de grados a decimal 
print("Bienvenidos al programa de conversiones:")
print("Seleccione un número del tipo de conversión que quieres realizar: ")
print("1. Grados, Minutos, Segundos -> Grados Decimales")
print("2. Grados Decimales -> Grados, Minutos, Segundos")
#Colocamos esta funcion para que el usuario escoga a traves de un valor entero, 1 o 2
seleccion = int(input("> "))
#Se coloca una condicionante si el usuario escoge la opcion 1, se le avisara por un mensaje y se le pedira que ingrese los valores que el desee.
if seleccion == 1:
    print("Has seleccionado convertir Grados, Minutos, Segundos a Grados Decimales")
    grados = int(input("Por favor ingresar grados: "))
    minutos = int(input("Por favor ingresar minutos: "))
    segundos = float(input("Por favor ingresar segundos: "))
#Se realizan los calculos respectivos para que se haga la conversion.    
    min_x = segundos/60 + minutos
#Se pone la funcion round para redondear a tres cifras.
    grados_x = round(((min_x)/60 + grados), 3)
#Se define una funcion referente al resultado final y dentro iran los mismos calculos por si hay cualquier error
    def gmd(grados_x):    
        min_x = segundos/60 + minutos
        grados_x = round(((min_x)/60 + grados), 3)
#Devuelve el resultado
        return (grados_x) 
#Se imprime el resultado con un mensaje de finalizacion  
    print ("Su resultados es: ", grados_x,"°")
    print ("FIN DEL PROCESO, GRACIAS")
#A traves de esta condicionante, si el usario escogio la opcion 2, se haran calculos de conversion para longitud y latitud.
elif seleccion == 2:
    print("Has seleccionado convertir Grados Decimales a Grados, Minutos, Segundos")
#Se pone la funcion float, ya que el usuario tendra que trabajar con decimales y no enteros.
    lat = float(input("Ingrese el valor de la latitud en decimales: "))
    lon = float(input("Ingrese el valor de la longitud en decimales: "))
#Se realizan los calculos para hacer las distintas conversiones, para latitud como longitud
    grados_lat = abs(int(lat))
    z = abs(float((lat)))-abs(int(lat))
    minutos = int(z * 60)
    minutos2 = float(z *60)
    a = abs(float((minutos2)))-abs(int(minutos2))
    segundos = float(a*60)

    grados_lon = abs(int(lon))
    deci_grados = abs(float((lon)))-abs(int(lon))
    minutos = int(deci_grados * 60)
    minutos2 = float(deci_grados *60)
    deci_grados_min2 = abs(float((minutos2)))-abs(int(minutos2))
    segundos = float(deci_grados_min2*60)
#Se define una funcion referente al resultado final y dentro iran los mismos calculos, longitud y latitud por si hay cualquier error

    def dms(lon,lat):
        grados_lon = abs(int(lon))
        deci_grados = abs(float((lon)))-abs(int(lon))
        minutos = int(deci_grados * 60)
        minutos2 = float(deci_grados *60)
        deci_grados_min2 = abs(float((minutos2)))-abs(int(minutos2))
        segundos = float(deci_grados_min2*60)
#Se colocan condicionantes en donde si el usuario escoge una cordenada mayor a 0, se le otorgara la direccion al este y en el caso contrario,
#si es negativo sera dad la direccion oeste    
    if lon >= 0:
        hem_lon = "E"
    else:
        hem_lon = "W"

        grados_lat = abs(int(lat))
        z = abs(float((lat)))-abs(int(lat))
        minutos = int(z * 60)
        minutos2 = float(z *60)
        a = abs(float((minutos2)))-abs(int(minutos2))
        segundos = float(a*60)
#Se vuelve a colocar condicionantes en donde si el usuario escoge una cordenada mayor a 0, se le otorgara la direccion al norte y en el caso contrario,
# la direccion sur
    if lat >= 0:
        hem_lat = "N"
    else:
        hem_lat = "S"
#Se imprimiran los resultados llamando a los calculos de longitud y latitud que se hicieron como un mensaje de finalizacion
    print('Su valor de latitud es:')
    y = f"{grados_lat}° {minutos}' {segundos:.2f}''{hem_lat}"
    print(y)
    
    print('Su valor de longitud es:')
    x = f"{grados_lon}° {minutos}' {segundos:.2f}'' {hem_lon}"
    print(x)
#Se pone esta condicionante por si el usuario no coloca la opcion 1 o 2, le aparecera un mensaje que escoga entre las dos.  
else:
    seleccion < 1 and seleccion > 2
    print("La opcion escogida no es valida :(. Escoger entre 1 y 2")