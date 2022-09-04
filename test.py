#!/usr/bin/python3
import sys
from JPEGTOPNG import convert_image_to_png

if __name__ == '__main__':
    print(convert_image_to_png(sys.argv[1], sys.argv[2]))
