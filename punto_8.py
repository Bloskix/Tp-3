file = open("ejercicio8.txt","w")
lista = ["texto de prueba"," ","segunda linea"," ","tercer linea\n","segundo parrafo p/l"," ","s/p segunda linea"," ","s/p tercer linea"]
file.writelines(lista)
file.close()
class read_txt_file:
    def __init__(self, text):
        self.text = text

    def count_lines(self):
        with open(self.text) as text:
            content = text.read()
        print(content)
        lines = []
        file = open(self.text,"r")
        for i in file:
            lines.append(i)
        n_of_lines = len(lines)
        print(f"There are: {n_of_lines} total lines")
    
    def count_words(self):
        with open(self.text) as file:
            content = file.read()
        words = content.split()
        num_words = len(words)
        print(f"There are: {num_words} total words")
    
    def count_letters(self):
        with open(self.text) as file1:
            content1 = file1.read()
        joined = content1.replace(" ","")
        total_chars = len(joined)
        print(f"There are: {total_chars} total characters")
text_example = read_txt_file("ejercicio8.txt.txt")
lines_amount = text_example.count_lines()
words_amount = text_example.count_words()
letters_amount = text_example.count_letters()
