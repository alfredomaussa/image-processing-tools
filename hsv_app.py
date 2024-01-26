import cv2
import numpy as np
from tkinter import Tk
from tkinter.filedialog import askopenfilename

# Función para no hacer nada en el callback de los sliders
def nothing(x):
    pass

# Función para ajustar el tamaño de la imagen para la visualización
def resize_image_for_display(image, max_display_height=800):
    """
    Redimensiona la imagen para la visualización, manteniendo la relación de aspecto,
    si su altura es mayor que max_display_height.
    """
    height, width = image.shape[:2]
    if height > max_display_height:
        scaling_factor = max_display_height / height
        resized_image = cv2.resize(image, None, fx=scaling_factor, fy=scaling_factor, interpolation=cv2.INTER_AREA)
        return resized_image
    return image

# Inicializa Tkinter y oculta la ventana principal
Tk().withdraw()

# Abre la ventana de diálogo para seleccionar un archivo de imagen y guarda la ruta seleccionada
image_path = askopenfilename()  # Muestra el diálogo para seleccionar un archivo

# Verifica si se seleccionó un archivo
if image_path:
    image = cv2.imread(image_path)

    # Convierte la imagen de BGR a HSV
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

    # Crea una ventana para los sliders
    cv2.namedWindow('HSV Tracker')

    # Creación de sliders para los valores mínimos y máximos de H, S y V
    cv2.createTrackbar('H Min', 'HSV Tracker', 0, 179, nothing)
    cv2.createTrackbar('H Max', 'HSV Tracker', 179, 179, nothing)
    cv2.createTrackbar('S Min', 'HSV Tracker', 0, 255, nothing)
    cv2.createTrackbar('S Max', 'HSV Tracker', 255, 255, nothing)
    cv2.createTrackbar('V Min', 'HSV Tracker', 0, 255, nothing)
    cv2.createTrackbar('V Max', 'HSV Tracker', 255, 255, nothing)

    while True:
        # Obtiene los valores de los sliders
        h_min = cv2.getTrackbarPos('H Min', 'HSV Tracker')
        h_max = cv2.getTrackbarPos('H Max', 'HSV Tracker')
        s_min = cv2.getTrackbarPos('S Min', 'HSV Tracker')
        s_max = cv2.getTrackbarPos('S Max', 'HSV Tracker')
        v_min = cv2.getTrackbarPos('V Min', 'HSV Tracker')
        v_max = cv2.getTrackbarPos('V Max', 'HSV Tracker')

        # Crea un rango de colores HSV basado en los valores de los sliders
        lower_hsv = np.array([h_min, s_min, v_min])
        upper_hsv = np.array([h_max, s_max, v_max])

        # Máscara que muestra solo los píxeles dentro del rango de los sliders
        mask = cv2.inRange(hsv, lower_hsv, upper_hsv)

        # Resultado de aplicar la máscara a la imagen original
        result = cv2.bitwise_and(image, image, mask=mask)

        # Muestra la imagen original, la máscara y el resultado
        cv2.imshow('Original', resize_image_for_display(image))
        cv2.imshow('Mask', resize_image_for_display(mask))
        cv2.imshow('Result', resize_image_for_display(result))

        # Rompe el bucle si se presiona 'q'
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Cierra todas las ventanas
    cv2.destroyAllWindows()
else:
    print("No se seleccionó ningún archivo.")
