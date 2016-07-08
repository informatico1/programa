import math
import os
import time


def resta(a,b):
    y=a-b
    return y

def suma(a,b):
    y=a+b
    return y

def seno(a):
    y=math.sin(a)
    return y

def coseno(a):
    y=math.cos(a)
    return y

def multiplicacion(a,b):
    y=a*b
    return y


def arcoseno(b):
    if b>=-1 and b<=1:
        z=math.asin(b)
        w=math.degrees(z)
        return w
    else:
        print("----------------------------------")
        print("usted ingreso un ángulo no valido, ya que el arcoseno esta en un rango unico de -1 hasta 1")


def arcocoseno(b):
    if b>=-1 and b<=1:
        z=math.acos(b)
        w=math.degrees(z)
        return w
    else:
        print("----------------------------------")
        print("usted ingreso un ángulo no valido, ya que el arcocoseno esta en un rango unico de -1 hasta 1")


def tang(d):
    x = math.tan(d)
    w = math.degrees(x)
    return w

def arctang(e):
    y = math.atan(e)
    z = math.degrees(y)
    return z


def xalax():
    os.system("clear")
    print("Modelo: X^×\n*X: base.\n*×: exponente.")
    print("\nIngrese valor de la base:")
    while True:
        try:
            base = float(input())
            break
        except ValueError:
            print("BASE Ingresado no valido, intente nuevamente...")
    print("\nIngrese valor del exponente:")
    while True:
        try:
            exp = float(input())
            break
        except ValueError:
            print("EXPONENTE Ingresado no valido, intente nuevamente...")
    print()
    print(base ** exp)



def division ():
    a=float(input("ingrese numero: "))
    b=float(input("ingrese numero: "))
    c=a/b
    time.sleep(1)
    print("el resultado es: ",c)

def raiz():
    e=float(input("ingrese numero: "))
    d=e**1/2
    os.system("cls")
    print("resultado es: ",d)
        




