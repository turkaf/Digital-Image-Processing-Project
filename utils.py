import numpy as np

def rescale(img):
    s = img.astype(float)
    s -= np.min(s)
    s /= np.max(s)
    return (s*255).astype(np.uint8)