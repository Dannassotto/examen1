import modules.corefiles as a
import json
def menuhistorial(op):
    title = """
    *************
    * HISTORIAL *
    *************
    """
    menuhistorialop= ('VISUALIZAR\n1. citas\n2.usuarios\n3.medicos\n4.salir')
    if(op!=4):
        print(title)
        print(menuhistorialop)
        try:
            opcion = int(input(">"))
        except ValueError:
            print("error de opcion")
            menuhistorialop(0)
        else:
            if opcion ==1:
                a.ReadFile= "data/usuarios.json"
                with open(a.ReadFile,"r") as uf:
                    datas= json.load(uf)
                    print(json.dumps(datas,indent=4)) 
                    menuhistorial(0)