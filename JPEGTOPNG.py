import sys
import os
from PIL import Image


def convert_image_to_png(path_to_get_image, path_to_store_image):

    path_to_get_image = os.path.realpath(path_to_get_image)

    for image_file in os.listdir(path_to_get_image):
        im = Image.open(os.path.join(path_to_get_image, image_file))

        path = os.path.join('./', path_to_store_image)

        if not os.path.exists(path):
            os.mkdir(path)

        path = os.path.join(path, image_file.split('.')[0] + '.'+'png')
        im.save(path, 'PNG')


convert_image_to_png(sys.argv[1], sys.argv[2])
