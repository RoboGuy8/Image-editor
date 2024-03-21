from PIL import Image
from filtry import green_filtr,blue_filtr,purple_filtr,iverted_filtr


while(True):
  print("""
---------------------------------------------------
Please chose wich filter to use by writing a number
1: purple
2: green
3: blue
4: surprise
Or type "exit" to interrupt the program
---------------------------------------------------
  """)
  filtr = input("filter number: ")

  if filtr == "1":
    purple_filtr()
  elif filtr == "2":
    green_filtr()
  elif filtr == "3":
    blue_filtr()
  elif filtr == "4":
    iverted_filtr()
  elif filtr == "exit":
    break
  else:
    print(f"Please chose valid number, not '{filtr}'")