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
    ("Es que me mata el recuerdo y solo pienso que pienso...\n", 0.03),
    ("Que te quites los Dolce & Gabbana ✨\n", 0.06),
    ("Yo solo siento que siento...\n", 0.05),
    ("Que no se que es lo que siento...\n", 0.05),
    ("Tanto nos pasó en una semana 💔\n", 0.05),
    ("Ya bloqueame si no es cierto, pero yo se, baby\n", 0.05),
    ("Cierto que ambos, mami , nos teniamos ganas\n", 0.05),
    ("Puede que sí reconozco, sé que apenas te conozco\n", 0.05),
    ("Lo que me mato fue tu mirada...\n", 0.05),
    ("Baby, bésame...\n", 0.05),
    ("Quiero que vuelvas a mis brazos pa' sentirnos eternos como la última vez\n", 0.09),
    ("Quiero confesarte te extraño\n", 0.06),
    ("Como un loco te pienso, yo sé que tú también\n", 0.08),
    ("Porfa, ma, ya vuelve conmigo, pero no como amigos\n", 0.06),
    ("Como la ultima vez\n", 0.06),
    ("Quiero confesarte te extraño, como un loco te pienso, yo sé que tú también\n", 0.08 ),
    ("Coquetaaaa\n", 0.05)
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