import math
import sys

def salir():
    """SALIR DEL PROGRAMA"""
    print("SALIENDO DEL PROGRAMA...")
    sys.exit()

def menu():
  print("Opciones:")
  print("1.  FORMULA GENERAL")
  print("2.  VOLUMEN DE UN CUBO")
  print("3.  FUERZA")
  print("4.  ACELERACION")
  print("5.  MASA")
  print("6.  DISTANCIA")
  print("7.  VELOCIDAD")
  print("8.  TIEMPO")
  print("9.  AREA CIRCULO")
  print("10. AREA CUADRADO")
  print("11. AREA TRIANGULO")
  print("0.  SALIR")
  

def formulaGeneral(a, b, c):
    """RESUELVE CON LA FORMULA GENERAL ax^2 + bx + c = 0"""
    return (-b + math.sqrt(b**2 - 4*a*c)) / (2*a), (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)

def volumenCubo(lado1):
    """VOLUMEN DE U CUBO USANDO UN LADO"""
    return lado1 ** 3
    
def fuerza(masa,aceleracion):
    """FUERZA=MASA*ACELERACION, SEGUNDA LEY DE NEWTON"""
    return masa * aceleracion

def aceleracion(masa,fuerza):
    """FUERZA=MASA*ACELERACION, SEGUNDA LEY DE NEWTON"""
    return fuerza/masa

def masa (aceleracion,fuerza):
    """FUERZA=MASA*ACELERACION, SEGUNDA LEY DE NEWTON"""
    return fuerza/aceleracion

def distancia(velocidad , tiempo):
    """DISTANCIA MRU"""
    return velocidad*tiempo

def velocidad(distancia, tiempo):
    """VELOCIDAD EN MRU"""
    return distancia/tiempo

def tiempo(distancia, velocidad):
    """TIEMPO EN MRU"""
    return distancia/velocidad

def areaCirculo(radio):
    """AREA=PI*(RADIO*RADIO)"""
    return math.pi*(radio*radio)

def circunferencia(diametro):
    """CIRCUNFERENCIA=DIAMETRO*PI"""
    return diametro*math.pi

def diametro(circunferencia):
    """DIAMETRO=CIRCUNFERENCIA/PI"""
    return circunferencia/math.pi

def radio(circunferencia):
    """RADIO=CIRUNFERENICA/(2*PI)"""
    return circunferencia/(2*math.pi)

def areaCuadrado(lado):
    """AREA=LADO*LADO"""
    return lado*lado

def areaTriangulo(base, altura):
    """AREA=(BASE*ALTURA)/2"""
    return (base*altura)/2

def areaRectangulo(lado1, lado2):
    """AREA=LADO1*LADO2"""
    return lado1*lado2

def salir ():
    """USA return 1"""
    return 1
