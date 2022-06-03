file = open("ejercicio7.txt","w")
lista = ["texto de prueba"," ","segunda linea"," ","tercer linea"]
file.writelines(lista)
file.close()
class Read_txt_file:
    def __init__(self, text, separator):
        self.text = text
        self.separator = separator

    def read_text(self):
        self.separator = input("Enter the separator you want to use: ")
        file = open(self.text, "r")
        read_lines = file.readlines()
        new_string = ' '.join(read_lines)
        my_list = new_string.split(" ")
        new_string1 = self.separator.join(my_list)
        print(new_string1)

text_example = Read_txt_file("ejercicio7.txt", " ")
print(text_example.read_text())
