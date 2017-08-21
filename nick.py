import cv2
from avgfilter import average_filter
import numpy as np
import os


def nick(image, window=(15, 15), k=-0.2, padding='edge'):
    image = image.astype(float)
    mean = average_filter(image, window, padding)

    mean_square = average_filter(image ** 2, window, padding)
    variance = mean_square - mean**2

    threshold = mean + k * np.sqrt(variance + mean**2)
    output = image > threshold   
    output = _binarize_color(output)
    return output


def _binarize_color(output):
    return output.astype(np.uint8) * 255


if __name__ == '__main__':
    import sys
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('path', help='Path to file being binarized')
    parser.add_argument('--window', help='Window size to use for mean calculation, HxW', default='15,15')
    parser.add_argument('--k', help='Niblack factor', type=float, default=-0.2)
    parser.add_argument('--padding', help='Padding type, passed to numpy', default='edge')
    parser.add_argument('--out', help='Alternative output path. Default is <path>_bw.ext')
    args = parser.parse_args()
    try:
        window_ = [int(x.strip()) for x in args.window.split(',')]
        if len(window_) != 2:
            raise ValueError('Invalid window size')
    except ValueError:
        parser.print_help()
        sys.exit(-1)
    print(args)
    x = cv2.imread(args.path)
    image_ = cv2.cvtColor(x, cv2.COLOR_BGR2GRAY)
    res = nick(image_, window_, args.k, args.padding)
    if args.out:
        output = args.out
    else:
        name, ext = os.path.splitext(sys.argv[1])
        output = name + '_bw' + ext
    cv2.imwrite(output, res)

