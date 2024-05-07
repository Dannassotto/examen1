import json
import os 

MY_DATABASE = "Datas_usuarios/"

def NewFile(*param):
    with open(MY_DATABASE,"w") as wf:
        json.dump(param[0],wf,indent=4)

def AddData(*param):
    data = list(param)
    with open(MY_DATABASE, "r+") as umu:
        file_data = json.load(umu)
        if len(param) > 1:
                    file_data[data[0]] = {}
                    file_data[data[0]].update({data[1]: data[2]})
        else:
            file_data.update(param[0])
        umu.seek(0)
        json.dump(file_data, umu, indent=4)
def ReadFile():
    with open(MY_DATABASE,"r") as uf:
        return json.load(uf)


def checkFile(*param):
    data= list(param)
    if(os.path.isfile(MY_DATABASE)):
        if(len(param)):
            data[0].update(ReadFile())
    else:
        if(len(param)):
            NewFile(data[0])

def updateFile(*param):
    with open(MY_DATABASE,'w') as fw:
        json.dump(param[0],fw,indent=4)