import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageTk
import cv2
import numpy as np

def choose_image():
    """Permite al usuario seleccionar una imagen y la muestra en la GUI."""
    global img_path, img
    img_path = filedialog.askopenfilename()
    if img_path:
        img = Image.open(img_path)
        img = img.resize((250, 250), Image.Resampling.LANCZOS)  # Uso de Resampling.LANCZOS para reemplazar ANTIALIAS
        img = ImageTk.PhotoImage(img)
        img_label.configure(image=img)
        img_label.image = img  # Mantener una referencia

def apply_clahe():
    """Aplica CLAHE a la imagen seleccionada y muestra el resultado."""
    if img_path is None:
        tk.messagebox.showerror("Error", "Please choose an image first")
        return
    
    # Leer la imagen seleccionada
    image = cv2.imread(img_path)
    if image is None:
        tk.messagebox.showerror("Error", "The selected file is not a valid image")
        return

    # Convertir la imagen a escala de grises
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Crear el objeto CLAHE
    clahe = cv2.createCLAHE(clipLimit=2.0, tileGridSize=(8,8))

    # Aplicar CLAHE a la imagen en escala de grises
    clahe_img = clahe.apply(gray)

    # Convertir la imagen CLAHE a formato RGB para mostrarla en Tkinter
    clahe_img = cv2.cvtColor(clahe_img, cv2.COLOR_GRAY2RGB)
    clahe_img = Image.fromarray(clahe_img)
    clahe_img = clahe_img.resize((250, 250), Image.Resampling.LANCZOS)
    clahe_img = ImageTk.PhotoImage(clahe_img)

    # Mostrar la imagen procesada
    result_label.configure(image=clahe_img)
    result_label.image = clahe_img  # Mantener una referencia

# Configuración inicial de Tkinter
root = tk.Tk()
root.title("CLAHE Image Processing")

# Variables globales
img_path = None
img = None

# Configuración de los widgets
img_label = tk.Label(root)
img_label.pack()

choose_btn = tk.Button(root, text="Choose Image", command=choose_image)
choose_btn.pack()

apply_btn = tk.Button(root, text="Apply CLAHE", command=apply_clahe)
apply_btn.pack()

result_label = tk.Label(root)
result_label.pack()

# Iniciar el bucle principal de la GUI
root.mainloop()
