import matplotlib.pyplot as plt
import numpy as np
from skimage import io


def show_colors(color_list):
    palette = np.array(color_list, dtype=np.uint8)

    res = np.reshape(np.arange(0,len(palette)),(9,9))

    io.imshow(palette[res])
    plt.show()
