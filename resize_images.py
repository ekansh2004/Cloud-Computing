import cv2
import os

input_folder = 'input_images'
output_folder = 'output_images'
target_width = 640
target_height = 480

os.makedirs(output_folder, exist_ok=True)

for filename in os.listdir(input_folder):
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        img_path = os.path.join(input_folder, filename)
        img = cv2.imread(img_path)

        if img is not None:
            resized_img = cv2.resize(img, (target_width, target_height))
            cv2.imwrite(os.path.join(output_folder, filename), resized_img)
            print(f'Resized {filename}')
        else:
            print(f'Failed to load {filename}')
