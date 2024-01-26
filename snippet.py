# %%
import cv2
import numpy as np
# %%
# Carga la imagen local
image_path = 'HSV_color_solid_cube.png'  # Reemplaza con la ruta de tu imagen
image = cv2.imread(image_path)
# %%
# Convierte la imagen a HSV
hsv_image = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

# Aplica el filtro HSV
mask = cv2.inRange(hsv_image, lower_hsv:=np.array([0,0,0]), upper_hsv:=np.array([55,255,255]))
result = cv2.bitwise_and(image, image, mask=mask)

result_rgb = cv2.cvtColor(result, cv2.COLOR_HSV2BGR)

cv2.imwrite("out.png",result)