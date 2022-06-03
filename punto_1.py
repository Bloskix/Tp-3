file = open("ejercicio1.txt","w")
file.write("texto de prueba")
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