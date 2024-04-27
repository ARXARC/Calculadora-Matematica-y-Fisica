import liberiaDef

while True:
    liberiaDef.menu()
    opcion=int(input("INGRESA OPCION: "))
    
    if opcion==0:
        liberiaDef.salir()

    elif opcion==1:
        a=float(input("INGRESE a: "))
        b=float(input("INGRESE b: "))
        c=float(input("INGRESE c: "))
        formulaGeneral=liberiaDef.formulaGeneral(a,b,c)
        print(f"X ES IGUAL A: {formulaGeneral}")

    elif opcion==2:
        lado1=float(input("INGRESE LADO:"))
        volumenCubo=liberiaDef.volumenCubo(lado1)
        print(f"EL VOLUMEN ES {volumenCubo}")

    elif opcion==3:
        masa=float(input("INGRESE MASA:"))
        aceleracion=float(input("INGRESE ACELERACION:"))
        fuerza=liberiaDef.fuerza(masa, aceleracion)
        print(f"FUERZA ES IGUAL A: {fuerza}")

    elif opcion==4:
        masa=float(input("INGRESE MASA:"))
        fuerza=float(input("INGRESE FUERZA:"))
        aceleracion=liberiaDef.aceleracion(masa,fuerza)
        print(f"ACELERACION ES IGUAL A: {aceleracion}")

    elif opcion==5:
        aceleracion=float(input("INGRESE ACELERACION:"))
        fuerza=float(input("INGRESE FUERZA:"))
        masa=liberiaDef.masa(aceleracion,fuerza)
        print(f"MASA ES IGUAL A: {masa}")

    elif opcion==6:
        velocidad=float(input("INGRESE VELOCIDAD:"))
        tiempo=float(input("INGRESE TIEMPO:"))
        distancia=liberiaDef.distancia(velocidad,tiempo)
        print(f"DISTANCIA ES IGUAL A: {distancia}")

    elif opcion==7:
        distancia=float(input("INGRESE DISTANCIA: "))
        tiempo=float(input("INGRESE TIEMPO:"))
        velocidad=liberiaDef.velocidad(distancia,tiempo)
        print(f"VELOCIDAD ES IGUAL A: {velocidad}")

    elif opcion==8:
        distancia=float(input("INGRESE DISTANCIA: "))
        velocidad=float(input("INGRESE VELOCIDAD: "))
        tiempo=liberiaDef.tiempo(distancia,velocidad)
        print(f"TIEMPO ES IGUAL A: {tiempo}")

    elif opcion==9:
        radio=float(input("INGRESE RADIO: "))
        areaCirculo=liberiaDef.areaCirculo(radio)
        print(f"AREA DEL CIRCULO ES IGUAL A: {areaCirculo}")

    elif opcion==10:
        lado=float(input("INGRESE LADO: "))
        areaCuadrado=liberiaDef.areaCuadrado(lado)
        print(f"AREA DEL CUADRADO ES IGUAL A: {areaCuadrado}")

    elif opcion==11:
        base=float(input("INGRESE BASE: "))
        altura=float(input("INGRESE ALTURA: "))
        areaTriangulo=liberiaDef.areaTriangulo(base,altura)
        print(f"AREA DEL TRIANGULO ES IGUAL A: {areaTriangulo}")
    else:
        print("OPCION NO VALIDA")