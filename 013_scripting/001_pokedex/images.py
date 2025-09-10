from PIL import Image, ImageFilter

img = Image.open(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\013_scripting\001_pokedex\Pokedex\pikachu.jpg")

print(img)
print(img.format)
print(img.size)
print(img.mode)

filtered_img = img.filter(ImageFilter.BLUR)
filtered_img.save(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\013_scripting\001_pokedex\Pokedex\blur.png", "png")

filtered_img = img.filter(ImageFilter.SMOOTH)
filtered_img.save(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\013_scripting\001_pokedex\Pokedex\smooth.png", "png")

filtered_img = img.filter(ImageFilter.SHARPEN)
filtered_img.save(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\013_scripting\001_pokedex\Pokedex\sharpen.png", "png")

filtered_img = img.convert('L') # it converts the image to grey scale, that is Black and White. Similarly RGB = Red Green Blue
filtered_img.save(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\013_scripting\001_pokedex\Pokedex\grey.png", "png")

img.show() # this opens the image in the default player

crooked_img = img.rotate(180)
crooked_img.save(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\013_scripting\001_pokedex\Pokedex\rotated.png", "png")

resized_img = img.resize((300,300)) # but this can ruin the aspect ratio hence we use thumbnail method
resized_img.save(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\013_scripting\001_pokedex\Pokedex\resized.png", "png")

box = (100,100,400,400)
cropped_img = img.crop(box)
cropped_img.save(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\013_scripting\001_pokedex\Pokedex\cropped.png", "png")

img.thumbnail((100,50)) # it will keep max. 50*50 aspect ratio, it can be 30*50, but it won't exceed 50 pixels
img.save(r"c:\Users\cnx36\Documents\7.Projects\1.ZeroToMastery\CompletePythonDeveloper\013_scripting\001_pokedex\Pokedex\thumbnail.png", "png")