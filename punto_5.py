file = open("ejercicio5.txt","w")
file.write("texto de prueba")
file.close()
class Copy_file():
    def __init__(self,archivo,accion):
        self.archivo = archivo
        self.accion = accion
    def copy_and_paste(self):
        file = open(self.archivo,self.accion)
        copia = file.read()
        file.close()
        n_file = open("copia5","w")
        n_file.writelines(copia)
        n_file.close()
        return print("Done")
copiar = Copy_file("ejercicio5.txt","r+")
copiar.copy_and_paste()
