import numpy as np
from math import floor, ceil


def average_filter(image, window=(15, 15), padding='edge'):
    m = window[0]
    n = window[1]

    rows, columns = image.shape[0], image.shape[1]
    width = ((floor((m+1)/2), ceil((m-1)/2)), (floor((n+1)/2), ceil((n-1)/2)))
    image_padded = np.pad(image, width, padding)
    t = _integral_image(image_padded.astype(float))

    image_i = _mean_values_by_lut(m, n, columns, rows, t)

    image_i = _window_average(image_i, m, n)

    return image_i


def _integral_image(image_d):
    return np.cumsum(np.cumsum(image_d, axis=1), axis=0)


def _mean_values_by_lut(window_h, window_w, columns, rows, t):
    return (t[window_h:rows + window_h, window_w:columns + window_w]
            + t[0:rows, 0:columns]
            - t[window_h:rows + window_h, 0:columns]
            - t[0:rows, window_w:columns + window_w])


def _window_average(image_i, m, n):
    return image_i / (m * n)
