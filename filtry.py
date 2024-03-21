from PIL import Image
def purple_filtr():
  obrazek = Image.open("mitata.jpg")
  sirka, vyska = obrazek.size
  x = 0
  while x < sirka:
      y = 0
      while y < vyska:
          r, g, b = obrazek.getpixel((x,y))
          r = r + r//2
          g = g//3
          b = 2*b
          obrazek.putpixel((x,y), (r , g, b))
          y += 1
      x += 1
  obrazek.show()

def green_filtr():
  obrazek = Image.open("mitata.jpg")
  sirka, vyska = obrazek.size
  x = 0
  while x < sirka:
      y = 0
      while y < vyska:
          r, g, b = obrazek.getpixel((x,y))
          r = r//3
          g = 2*g
          b = b//2
          obrazek.putpixel((x,y), (r , g, b))
          y += 1
      x += 1
  obrazek.show()

def blue_filtr():
  obrazek = Image.open("mitata.jpg")
  sirka, vyska = obrazek.size
  x = 0
  while x < sirka:
      y = 0
      while y < vyska:
          r, g, b = obrazek.getpixel((x,y))
          r = r//2
          g = g//3
          b = 2*b
          obrazek.putpixel((x,y), (r , g, b))
          y += 1
      x += 1
  obrazek.show()

def iverted_filtr():
  obrazek = Image.open("mitata.jpg")
  sirka, vyska = obrazek.size
  x = 0
  while x < sirka:
      y = 0
      while y < vyska:
          r, g, b = obrazek.getpixel((x,y))
          obrazek.putpixel((x,y), (b , r, g))
          y += 1
      x += 1
  obrazek.show()