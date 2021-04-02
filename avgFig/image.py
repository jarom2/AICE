from PIL import Image as im
import numpy as np

avg_4 = np.load("avg_4.npy")
avg_10 = np.load("avg_10.npy")
avg_32 = np.load("avg_32.npy")
avg_C = np.load("avg_C.npy")

img_4 = im.fromarray(avg_4*255)
img_4 = img_4.convert("L")
img_4.save("img_4.jpg")
