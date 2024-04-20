import sys
from tkinter import *
from PIL import Image, ImageDraw
import tensorflow as tf
import numpy as np

drawing_area = ""
x, y = None, None
count = 0
image_cont = 0
image_names = "canvas_"
pil = Image.new("L", (500, 500), "white")  # Cambiado "1" a "L" para guardar en escala de grises
draw = ImageDraw.Draw(pil)

def quitar(event):
    sys.exit()

def limpiar(event):
    global drawing_area, pil, draw
    drawing_area.delete("all")
    pil = Image.new("L", (500, 500), "white")  # Cambiado "1" a "L"
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
    file_name = image_names + str(image_cont) + ".jpg"
    pil_resized = pil.resize((28, 28))  # Redimensionar la imagen a 28x28 para que coincida con el modelo
    pil_resized.save(file_name)
    # Realizar la predicción con el modelo
    model = tf.keras.models.load_model('modelo_mnist.h5')
    img = tf.keras.preprocessing.image.load_img(file_name, color_mode='grayscale', target_size=(28, 28))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array = img_array / 255.0  # Normalizar los valores de píxeles
    # Realizar la predicción con el modelo
    prediction = model.predict(img_array)
    # Convertir la salida de la predicción a texto
    predicted_class = np.argmax(prediction)
    print("La neurona predice:", predicted_class)

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
