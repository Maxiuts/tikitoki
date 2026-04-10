import time
import sys
# Colores ANSI
colores = [
    "\033[91m",  # rojo
    "\033[92m",  # verde
    "\033[93m",  # amarillo
    "\033[94m",  # azul
    "\033[95m",  # magenta
    "\033[96m",  # cyan
    "\033[97m",  # blanco
]

reset = "\033[0m"

letras = [
    ("Y hace tiempo\n", 0.05),
    ("que no venias a mi cabeza\n", 0.06),
    ("Pero ya van par de cervezas\n", 0.06),
    ("y me acordé de cómo tú me besas\n", 0.07),
    ("de to' los polvos encima de la mesa\n", 0.06),
    ("y en el carro, la playa, el motel\n", 0.06),
    ("En casa de tu pai cuando yo te iba a ver\n", 0.06),
    ("Las veces que tu mai nos llegó a coger\n", 0.06),
    ("Tú brincando mojaíta, sudando Chanel\n", 0.06),
    ("Yo sé que lo nuestro es cosa de ayer\n", 0.05),
    ("Y me pone contento que te vaya bien con el\n", 0.05),
    ("Yo ni te extrañaba ni te quería ver\n", 0.06),

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