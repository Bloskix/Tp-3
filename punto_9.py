file = open("ejercicio9.txt","w")
lista = ["texto de prueba"," ","segunda linea"," ","tercer linea\n","segundo parrafo p/l"," ","s/p segunda linea"," ","s/p tercer linea"]
file.writelines(lista)
file.close()
class read_text_file:
    def __init__(self, text, expression):
        self.text = text
        self.expression = expression
    
    def read_lines(self):
        file = open(self.text, "r")
        for line in file:
            if self.expression in line:
                print(line)

expression1 = str(input("Enter the expression you want to look for: "))
example = read_text_file("ejercicio9.txt", expression1)
example.read_lines()
