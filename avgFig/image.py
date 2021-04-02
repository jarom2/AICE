from PIL import Image as im
import numpy as np

avg_4 = np.load("avg_4.npy")
avg_10 = np.load("avg_10.npy")
avg_32 = np.load("avg_32.npy")
avg_C = np.load("avg_C.npy")

img_4 = im.fromarray(avg_4*255)
img_4 = img_4.convert("L")
img_4.save("img_4.jpg")

img_10 = im.fromarray(avg_10*255)
img_10 = img_10.convert("L")
img_10.save("img_10.jpg")

img_32 = im.fromarray(avg_32*255)
img_32 = img_32.convert("L")
img_32.save("img_32.jpg")  

img_C = im.fromarray(avg_C*255)
img_C = img_C.convert("L")
img_C.save("img_C.jpg")  

