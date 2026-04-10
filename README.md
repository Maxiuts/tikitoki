# tikitoki
script para tiktoks

si quieres usar el codigo para 
cualquier otra cancion, solo debes de modificar la letra

("Pero ya van par de cervezas\n", 0.06),          lo que hace el numero despues de la letra, es la velocidad 

0.01 - Muy rapido
0.03 - Velocidad normal
0.05 - Mas lento

asi es como funciona

time.sleep(0.4)  # pausa entre líneas
Esta linea es el descanso que hay entre las letras,
a mayor el numero, mas lenta la continuacion de las letras.

# 🎧 tikitoki

Script en Python para crear textos tipo *letra animada* estilo TikTok directamente en la terminal.

Minimalista, limpio y con flow ✨

---

## 🚀 ¿Qué hace?

Simula el efecto de texto que se va escribiendo poco a poco (tipo karaoke / storytelling), ideal para:

- Letras de canciones
- Frases aesthetic
- Intros tipo “cinematográficas”

---

## 🛠️ ¿Cómo usarlo?

Solo necesitas modificar la letra dentro del arreglo:

```python
("Pero ya van par de cervezas\n", 0.06),
```

### 📌 ¿Qué significa el número?

Es la **velocidad de escritura** (delay por letra):

| Velocidad | Valor |
|----------|------|
| Muy rápido ⚡ | `0.01` |
| Normal 👌 | `0.03` |
| Lento 🐢 | `0.05` |

---

## ⏱️ Pausa entre líneas

```python
time.sleep(0.4)
```

Esto controla el tiempo de espera entre cada línea.

- Menor valor → más fluido
- Mayor valor → más dramático

---

## 🎨 Personalización

Puedes ajustar fácilmente:

- ✍️ Texto (letras o frases)
- ⏳ Velocidad por línea
- 🎭 Emojis para dar énfasis
- 🎬 Ritmo general del script

---

## 💡 Ideas

- Hacer intros para videos
- Crear dedicatorias personalizadas
- Generar contenido para redes
- Usarlo como base para proyectos más grandes

---

## 🧠 Tip pro

Menos es más.

Un solo color, pocos emojis y buen timing hacen que se vea mucho más profesional 👀

---

## 📦 Requisitos

- Python 3

---

## ▶️ Ejecutar

```bash
python3 tu_script.py
```

---

Hecho para experimentar, crear y jugar con el estilo 😎