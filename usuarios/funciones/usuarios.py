import modules.corefiles as us
def RUsuario(op):
    title = """
    *****************************
    *  REGISTRO DE USUARIOS    *
    *****************************
    """ 
    print(title)
    try:
        Identificacion = int(input("ingrese Nro de Identificacion : "))

        Nombre = input("ingrese Nombre:  ")
        Apellido = input("ingrese Apellido:  ")
        Ntelefono = input("ingrese Nro de telefono: ")
        ubicacion = input("Ingrese la fecha de nacimiento (D/M/A): ")
        direccion, ciudad, logitud,latitud = ubicacion.split('/')
        ubicacion = f"{direccion}/{ciudad}/{logitud}/{logitud}/{latitud}"
        email=input("ingrse el email")
        edad=input('ingrese edad')
        ocupacion=("ingrese ocupacion")

        usuarios ={
            'Identificacion': Identificacion,
            'Nombre': Nombre,
            'Apellido' : Apellido,
            'ubicacion' : ubicacion,
            'email' : email,
            'edad' : edad,
            'ocupacion' :ocupacion
        }
    except ValueError:
        print("opcion invalidad")
        RUsuario(0)
    
    us.AddData('Datas_usuarios', Identificacion,usuarios)
    if(bool(input('desea registrar otro Usuario S(si) o Enter (No)'))):
        RUsuario(0)
    

