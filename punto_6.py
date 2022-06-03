file = open("ejercicio2.txt","w")
lista = ["texto de prueba\n","segunda linea\n","tercer linea"]
file.writelines(lista)
file.close()
class Text_n_reader:
    def __init__(self,archivo,accion,n):
        self.archivo = archivo
        self.accion = accion
        self.n = n
    def read (self):
        file = open(self.archivo,self.accion)
        list = []
        list = file.readlines()
        new_list = []
        for i in list:
            i = i.strip("\n")
            new_list.append(i)
        return new_list[0:self.n]
leer = Text_n_reader("ejercicio2.txt","r",1)
print("cuantas lineas del archivo desea leer (maximo 3)")
leer.n = int(input())
print(leer.read())
file.close()
