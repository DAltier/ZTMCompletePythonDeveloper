from translate import Translator

with open(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\010_file_io.py\translate.txt", mode = 'r') as my_file:
    text = my_file.read()

translator= Translator(to_lang="pt")
translation = translator.translate(text)
with open(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\010_file_io.py\translated-text.txt", mode = 'w') as my_file2:
    my_file2.write(translation)

print(translation)