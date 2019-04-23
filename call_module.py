import matplotlib.pyplot as plt
import cv2
import numpy as np

from cardash_func import *

filename="/home/farman/AIQ/darknet/data.txt"
image = cv2.imread('/home/farman/AIQ/darknet/car_dash/1.jpg')


draw_center_lines(image, filename)
check_blue_symbols(image)
check_green_symbols(image)
