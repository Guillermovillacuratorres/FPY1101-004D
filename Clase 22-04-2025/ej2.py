nombre = "Juanito"
edad = 15
casado = False
"""
print("Hola",nombre,"bienvenido a python")
print("Hola "+nombre+" bienvenido a python")
print(f"Hola {nombre}, tú ❤️ edad' es {edad}, bienvenido a python 😍😍 🐍🐍🐍")

"""

texto = "El trozo de texto estándar de Lorem Ipsum usado desde el año 1500 es reproducido debajo para aquellos interesados. Las secciones 1.10.32 y 1.10.33 de de Finibus Bonorum et Malorum por Cicero son también reproducidas en su forma original exacta, acompañadas por versiones en Inglés de la traducción realizada en 1914 por H. Rackham."
#        0123456789   
print(texto[11:17])
print(len(texto)-1)
print(texto[330])

print(texto.lower())
print(texto.upper())

txt = "    hola, como estas?    "
print(txt.capitalize())

print(texto.upper().replace("A","@"))
print(texto.find("TEXTO"))
print(texto.split())
print(txt.strip())