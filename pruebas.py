import time
import sys
# Colores ANSI
colores = [
    "\033[90m",  # gris
]

reset = "\033[0m"

letras = [
    ("Vi que viste mi story y subiste una pa' mi \n", 0.07),
    ("Yo que me iba a dormir, ey \n", 0.05),
    ("En la disco habían mil \n", 0.05),
    ("Y yo bailando contigo en mi mente \n", 0.05),
    ("Aunque sé que no debo \n", 0.08),
    ("Pensar en ti, bebé, pero cuando bebo 🍻\n", 0.09),
    ("Me viene tu nombre, tu cara, tu risa y tu pelo, ey \n", 0.09),
    ("Dime donde tu estas que yo por ti cojo un vuelo ✈️\n", 0.09),
    ("Y a Yonaguni le llego \n", 0.09)
]

def escribir(linea, velocidad, color):
    print(color, end="")  # aplica solo gris sin efecto tenue
    for letra in linea:
        print(letra, end="", flush=True)
        time.sleep(velocidad)
    print(reset, end="")

for i, (linea, velocidad) in enumerate(letras):
    color = colores[i % len(colores)]  # rota colores
    escribir(linea, velocidad, color)
    time.sleep(0.4)