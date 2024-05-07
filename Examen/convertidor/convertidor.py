def convertidor(op):
    title = """
    ********
    * MENU *
    ********
    """
    convertidorop = '1. dolar a pesos\n2. pesos a euros\n3. euros a pesos\n4. pesos a yenes '
    if(op !=4):
        print(title)
        print(convertidorop)
        try:
            opcion = int(input(">"))
        except ValueError:
            print("La opción no tiene formato adecuado")
            convertidor(0)
        else:
            if opcion == 1:
                dolar_a_pesos()
            elif opcion == 2:
                pesos_a_euros()
            elif opcion == 3:
                euros_a_pesos()
            elif opcion == 4:
                pesos_a_yenes()
            else:
                print("Espero que hayas tenido un buen servicio")
            
                convertidor(op)


def dolar_a_pesos():
    pesos=int(input("ingrese el valor en pesos"))
    dolar=3944
    pesos=pesos/dolar


def pesos_a_euros():
    pesos=int(input("ingrese en pesos"))
    euros=4279
    pesos= pesos/euros
def euros_a_pesos():
    euros=input("ingrese el valor en euros")
    pesos=4279
    euros=pesos*euros

def pesos_a_yenes():
    yenes=int(input("ingrese el valor en yenes"))
    pesos=26.30
    yenes=pesos*yenes

convertidor(0)
