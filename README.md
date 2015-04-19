# thresholding
Nick's binarization derives thresholding formula from the basic Niblack algorithm, the parent of many local image thresholding methods. The major advantage of Nick's method over Niblack is that it considerably improves binarization for "white" and light page images by shifting down the binarization threshold.

The method description and comparison with other methods is available at http://dx.doi.org/10.1117/12.805827

This is the python code for doing said binarisation.

translated from MATLAB version: http://in.mathworks.com/matlabcentral/fileexchange/42104-nick-local-image-thresholding
