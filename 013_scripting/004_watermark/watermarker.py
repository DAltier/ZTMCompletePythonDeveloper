import PyPDF2

template = PyPDF2.PdfReader(open('c:/Users/cnx36/Documents/7.Projects/1.ZeroToMastery/CompletePythonDeveloper/013_scripting/004_watermark/merged.pdf', 'rb'))
watermark = PyPDF2.PdfReader(open('c:/Users/cnx36/Documents/7.Projects/1.ZeroToMastery/CompletePythonDeveloper/013_scripting/004_watermark/water.pdf', 'rb'))
output = PyPDF2.PdfWriter()

for i in range(len(template.pages)):
    page = template.pages[i]
    page.merge_page(watermark.pages[0])
    output.add_page(page)
 
with open('c:/Users/cnx36/Documents/7.Projects/1.ZeroToMastery/CompletePythonDeveloper/013_scripting/004_watermark/watermaked_output.pdf', 'wb') as outputFile:
    output.write(outputFile)