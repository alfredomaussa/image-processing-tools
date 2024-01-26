# Importamos cv2 para el procesamiento de imágenes
import cv2

def read_image(filepath):
    """
    Lee una imagen desde un archivo especificado.

    Parámetros:
    - filepath: Ruta del archivo de la imagen.

    Retorna:
    - image: La imagen leída como un array de numpy.
    """
    # Cargamos la imagen usando cv2.imread
    image = cv2.imread(filepath)
    return image

def show_image(image, window_name='Image'):
    """
    Muestra una imagen en una ventana.

    Parámetros:
    - image: La imagen a mostrar.
    - window_name: Nombre de la ventana en la que se mostrará la imagen.
    """
    # Mostramos la imagen usando cv2.imshow
    cv2.imshow(window_name, image)
    # Esperamos a que el usuario presione una tecla para cerrar la ventana
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def convert_to_grayscale(image):
    """
    Convierte una imagen a escala de grises.

    Parámetros:
    - image: La imagen a convertir.

    Retorna:
    - gray_image: La imagen convertida a escala de grises.
    """
    # Convertimos la imagen a escala de grises usando cv2.cvtColor
    gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    return gray_image
