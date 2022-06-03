file = open("ejercicio2.txt","w")
lista = ["texto de prueba\n","segunda linea\n","tercer linea"]
file.writelines(lista)
file.close()
class Text_reader:
    def __init__(self,archivo,accion):
        self.archivo = archivo
        self.accion = accion
    def read (self):
        file = open(self.archivo,self.accion)
        return file.readlines()
leer = Text_reader("ejercicio1.txt", "r")
print(leer.read())
file.close()