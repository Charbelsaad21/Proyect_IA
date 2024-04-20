import sys
from tkinter import *
from PIL import Image, ImageDraw

drawing_area = ""
x, y = None, None
count = 0
image_cont = 0
image_names = "canvas_"
pil = Image.new("1", (500, 500), "white")
draw = ImageDraw.Draw(pil)

def quitar(event):
    sys.exit()

def limpiar(event):
    global drawing_area, pil, draw
    drawing_area.delete("all")
    pil = Image.new("1", (500, 500), "white")
    draw = ImageDraw.Draw(pil)

def graficar(event):
    global drawing_area, x, y, count, draw
    newx, newy = event.x, event.y
    if x is None:
        x, y = newx, newy
        return
    count += 1
    drawing_area.create_line((x, y, newx, newy), width=5, smooth=True)
    draw.line((x, y, newx, newy), width=10)
    x, y = newx, newy

def graficar_finalizo(event):
    global x, y
    x, y = None, None

def guardar(event):
    global pil, image_names, image_cont
    image_cont += 1
    file_name = image_names + str(image_cont) + "canvas_1.jpg"
    pil_resized = pil.resize((300, 300))
    pil_resized.save(file_name)

def main():
    global drawing_area
    win = Tk()
    win.title("Lienzo Para Graficar")
    drawing_area = Canvas(win, width=500, height=500, bg="white")
    drawing_area.bind("<B1-Motion>", graficar)
    drawing_area.bind("<ButtonRelease-1>", graficar_finalizo)
    drawing_area.pack()
    b1 = Button(win, text="Salir", bg="red")
    b1.pack()
    b1.bind("<Button-1>", quitar)
    b2 = Button(win, text="Limpiar", bg="blue")
    b2.pack()
    b2.bind("<Button-1>", limpiar)
    b3 = Button(win, text="Guardar", bg="green")
    b3.pack()
    b3.bind("<ButtonRelease-1>", guardar)  # Cambiado de "<Button-1>" a "<ButtonRelease-1>"
    win.mainloop()

if __name__ == "__main__":
    main()
