
import numpy as np

def calculate_mean(data):
    if not data:
        return 0
    return np.mean(data)

def calculate_std(data):
    if not data:
        return 0
    return np.std(data)
