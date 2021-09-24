import numpy as np
import os
import sys
import skimage.transform
import html
import intrinsic
from skimage import color
import imageio

tag = "teabag1"
image = imageio.imread(os.path.join("data", tag, "diffuse.png"))
#image = color.gray2rgb(image)
# mask = np.ones((image.shape[0], image.shape[1]))
mask = imageio.imread(os.path.join("data", tag, "mask.png"))
color_t = 0.2
gray_t = 0.18
shading, refl = intrinsic.color_retinex(image, mask, gray_t, color_t, L1=True)
imageio.imwrite(os.path.join("results", "{}_shade_{}_{}.png".format(tag, gray_t, color_t)), shading)
imageio.imwrite(os.path.join("results", "{}_refl_{}_{}.png".format(tag, gray_t, color_t)), refl)