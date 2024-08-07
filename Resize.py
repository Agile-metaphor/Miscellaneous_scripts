from PIL import Image, ImageOps
from random import randrange
from tqdm import tqdm
import os

target_size = 1080
original_path = 'D:\\Resize\\Extracted\\'
resize_path = 'D:\\Resize\\Resized\\'
folder_arr = ['Extracted']


def random_crop(folder, image_name):
    img1 = Image.open(folder + '\\' + image_name)
    img_size = img1.size
    x_max = img_size[0] - target_size
    y_max = img_size[1] - target_size

    for i in range(10):
        random_x = randrange(0, x_max//2 + 1) * 2
        random_y = randrange(0, y_max//2 + 1) * 2

        area = (random_x, random_y, random_x + target_size, random_y + target_size)
        c_img = img1.crop(area)

        #fit_img_h = ImageOps.fit(c_img, (512, 512), Image.ANTIALIAS)
        #fit_img_h.save('{}/{}_{}_{}'.format(original_path, folder, i, image_name))

        fit_img_l = ImageOps.fit(c_img, (256, 256), Image.ANTIALIAS)
        fit_img_l.save('{}/{}'.format(resize_path, image_name))

for folder in folder_arr:
    img_names = os.listdir(folder)
    
    for name in tqdm(img_names):
        random_crop(folder, name)