from PIL import Image
obrazek = Image.open("mitata.jpg")
sirka, vyska = obrazek.size
x = 0
while x < sirka:
    y = 0
    while y < vyska:
        r, g, b = obrazek.getpixel((x,y))
        prumer = int((r+g+b)/3)
        r = r + r//2
        g = g//3
        b = 2*b
        obrazek.putpixel((x,y), (r , g, b))
        #if prumer > 150:
         #   obrazek.putpixel((x,y), (255, 255, 255))
        #else:
         #   obrazek.putpixel((x,y), (0, 0, 0))
        y += 1
    x += 1
obrazek.show()

