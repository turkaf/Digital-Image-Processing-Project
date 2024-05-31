import numpy as np

def stack(*args):
    return np.hstack(args)

def rescale(img):
    s = img.astype(float)
    s -= np.min(s)
    s /= np.max(s)
    return (s*255).astype(np.uint8)