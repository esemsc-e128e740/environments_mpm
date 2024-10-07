import sys
import pathlib

sys.path.append(str(pathlib.Path(__file__).parent.parent.resolve()))

from envtest import smooth_image

from scipy import misc
import matplotlib.pyplot as plt

image = misc.ascent()
sigma = 5

smoothed_image = smooth_image(image, sigma)

f = plt.figure()
f.add_subplot(1, 2, 1)
plt.imshow(image)
f.add_subplot(1, 2, 2)
plt.imshow(smoothed_image)
plt.show(block=True)
