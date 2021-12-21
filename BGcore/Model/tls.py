import pickle
def param2file(param):
    import json
    f = open("cparam.dat","w+")
    print("Hello")
    f.write(json.dumps(param,sort_keys=True, indent=4))
    f.close()


def importParam():
    import json
    f = open("cparam.dat","r")
    if f.mode =='r':
        contents = f.read()
        param = json.loads(contents)
    return param

def dump2tex(param):
    f = open("param.tex","w+")
    for i in param:
        string = '\\n'+"ewcommand{\\"+i+"}{"+str(param[i])+"}"
        f.write(string+"\n")
    f.close()



def importPICKLE(name):
    f = open(name, "rb")
    return pickle.load(f)
    
