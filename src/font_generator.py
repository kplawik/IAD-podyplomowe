import cv2
import copy
import numpy as np
from PIL import Image, ImageFont, ImageDraw
import sys
import os

def make_noise(noise_level, image_bin, width, height):
    np.random.seed(123)
    image_noise = copy.deepcopy(image_bin)
    for i in range(width):
        for j in range(height):
            if np.random.rand() <= noise_level / 100:
                image_noise[i][j] = 255 - image_noise[i][j]
    return image_noise

#w h x y font_file letter noise_level output_directory
width = int(sys.argv[1])
height = int(sys.argv[2])
x = int(sys.argv[3])
y = int(sys.argv[4])
font_file = sys.argv[5]
letter = sys.argv[6]
noise_level = int(sys.argv[7])
output_directory = sys.argv[8]

os.makedirs(output_directory, exist_ok=True)
file = open(output_directory+'/description.txt', 'a')
image = Image.new('RGB', (width, height), (255, 255, 255))
draw = ImageDraw.Draw(image)
font = ImageFont.truetype(font_file, 64)

draw.text((x, y), letter, font = font, fill = (0, 0, 0))
cv_color_image = np.asarray(image)
cv_gray_image = cv2.cvtColor(cv_color_image, cv2.COLOR_BGR2GRAY)
cv_noise_image = make_noise(noise_level, cv_gray_image, width, height)

cv2.imwrite(output_directory+'/'+letter+'.png', cv_noise_image)
file.write(letter+'.png:letter '+letter+', noise level '+str(noise_level)+'%\n')
file.close()