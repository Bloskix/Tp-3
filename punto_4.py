file = open("ejercicio4.txt","w")
lista = ["texto de prueba\n","segunda linea\n","tercer linea"]
file.writelines(lista)
file.close()
class Text_reader_save:
    def __init__(self,archivo,accion):
        self.archivo = archivo
        self.accion = accion
    def readandsave(self):
        file = open(self.archivo,self.accion)
        list = []
        list = file.readlines()
        new_list = []
        for i in list:
            i = i.strip("\n")
            new_list.append(i)
        return new_list
leer = Text_reader_save("ejercicio4.txt","r")
print(leer.readandsave())
