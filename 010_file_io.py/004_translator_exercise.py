from translate import Translator

with open(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\010_file_io.py\translate.txt", mode = 'r') as my_file:
    text = my_file.read()

translator= Translator(to_lang="es")
translation = translator.translate(text)

print(translation)