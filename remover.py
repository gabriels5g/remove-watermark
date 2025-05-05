import cv2
import numpy as np
import os

input_folder = 'imagens_com_marca'
output_folder = 'imagens_sem_marca'

if not os.path.exists(output_folder):
    os.makedirs(output_folder)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        image_path = os.path.join(input_folder, filename)
        image = cv2.imread(image_path)
        height, width = image.shape[:2]

        mask = np.zeros((height, width), dtype=np.uint8)

        
        margem_lateral = 100   
        margem_inferior = 100  

        
        mask[:, 0:margem_lateral] = 255
       
        mask[:, width - margem_lateral:] = 255
        
        mask[height - margem_inferior:, :] = 255

        
        resultado = cv2.inpaint(image, mask, 3, cv2.INPAINT_TELEA)

        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, resultado)

print("Marcas dos lados e da parte de baixo foram removidas!")
