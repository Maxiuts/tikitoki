import time
import sys
# Colores ANSI
colores = [
    "\033[97m",  # blanco
    "\033[30m"  # negro
]

reset = "\033[0m"

letras = [
    ("Y te miro bailar de lejitos\n", 0.05),
    ("Si me pego, tú me deces \"Vete\"\n", 0.05),
    ("Pero miro que dicen tus ojos\n", 0.05),
    ("y se miran felices de verme\n", 0.05),
    ("las palabras y hechizos nos sobran\n", 0.06),
    ("Desde que ella dejo de quererme\n", 0.05),
    ("y para encontrarte a mi, yo tuve que perderte\n", 0.07)
]

def escribir(linea, velocidad, color):
    print(color, end="")  # aplica color
    for letra in linea:
        print(letra, end="", flush=True)
        time.sleep(velocidad)
    print(reset, end="")  # resetea color

for i, (linea, velocidad) in enumerate(letras):
    color = colores[i % len(colores)]  # rota colores
    escribir(linea, velocidad, color)
    time.sleep(0.4)  # pausa entre líneas