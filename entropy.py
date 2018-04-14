import numpy as np

def entropy(ps):
    items = ps * np.log(ps)
    return -np.sum(items)