# a for append, w for write, r+ for read and write
with open(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\010_file_io.py\test.txt", mode = 'a') as my_file:
    text = my_file.write("I am HAPPY!")
    print(text)     # it prints the no. of letters written into the file
    
    
with open(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\010_file_io.py\test.txt", mode = 'r') as my_file:
    print(my_file.read())