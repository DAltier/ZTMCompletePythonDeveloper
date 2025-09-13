import PyPDF2

with open(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\013_scripting\002_pdf\dummy.pdf", 'rb') as file:      
# 'rb' is read binary, for pdf we append 'b' to it.
# so it converts the file to binary and PyPDF2 works with binary files.
    reader = PyPDF2.PdfReader(file)
    print(file)
    print(reader)
    print(len(reader.pages))
    print(reader.pages[0])

    page = reader.pages[0]
    page.rotate(90)
    writer = PyPDF2.PdfWriter()
    writer.add_page(page)

    with open(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\013_scripting\002_pdf\rotated.pdf", 'wb') as new_file:
        writer.write(new_file)