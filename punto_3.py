file = open("ejercicio3.txt","w")
file.write("texto de prueba")
file.close()
class Text_reader_add:
    def __init__(self,archivo,accion):
        self.archivo = archivo
        self.accion = accion
    def add (self,text):
        file = open (self.archivo,self.accion)
        file.write(text)
        return file.readlines()
leer = Text_reader_add("ejercicio3.txt","r+")
print("ingrese un texto")
texto = str(input())
print(leer.add(texto))

