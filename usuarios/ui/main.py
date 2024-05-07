import funciones.usuarios as u
import ui.historial as e
import modules.corefiles as t
def mainMenu(op):
    title= """
    ***************************
    *  MENU DE ADMINISTRACION    * 
    ***************************
    """
    mainMenuOp= "1. Gestion de citas\n2 Registros de Usuarios\n3 Registro especialista\n4 Historial usuarios"
    if(op!=4):
        print(title)
        print(mainMenuOp)
        try:
            opcion = int(input(">"))
        except ValueError:
            print("error de opcion")
            mainMenu(0)
        else:
            if opcion ==1:
                u.RUsuario
            elif opcion == 2:
                e.menuhistorial(0)
            else:
                    print("La opcion no es correcta")
                    mainMenu(opcion)
if __name__=="__main__":
    t.MY_DATABASE= "data/usuarios.json"
    t.checkFile
    mainMenu(0)                   
