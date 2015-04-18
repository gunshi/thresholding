

import numpy as np
from math import floor,ceil


def averagefilter(image, *args):

    numvarargs = len(args)
    if numvarargs > 2:
        print('myfuns:somefun2Alt:TooManyInputs')
        return
 
    optargs = [[3,3],0]           # set defaults for optional inputs
    optargs[0:numvarargs] = args
    window, padding = optargs[:] # use memorable variable names
    m = window[0]
    n = window[1]

    # Initialization.
    rows,columns = image.shape[0],image.shape[1]

    # If we have to calculate the integral image, calculate it.
    if isinstance(padding,basestring) or isinstance(padding,int):
        # Pad the image.

	      imagePP=np.pad(image,((floor((m+1)/2),ceil((m-1)/2)), (floor((n+1)/2),ceil((n-1)/2))),padding) 

      	imageD = imagePP.astype(float)

        # Calculate the integral image - the sum of numbers above and left.
        t = np.cumsum(np.cumsum(imageD,axis=1),axis=0)




    else:
        # Cut the integral image from the potentially bigger integral image.
        intm = np.size(padding,0) - rows						
        intn = np.size(padding,1) - columns

        deltaMPre = floor((intm+1)/2) - floor((m+1)/2)  ##done minus 1 here
        deltaMPost = ceil((intm-1)/2) - ceil((m-1)/2)
    
        deltaNPre = floor((intn+1)/2) - floor((n+1)/2)  ##done minus 1 here
        deltaNPost = ceil((intn-1)/2) - ceil((n-1)/2)
        
        t = padding[deltaMPre : end-deltaMPost, deltaNPre : end-deltaNPost]


    # Calculate the mean values from the look up table 't'.
    imageI = t[m:rows+m, n:columns+n] + t[0:rows, 0:columns] - t[m:rows+m, 0:columns] - t[0:rows, n:columns+n]  ##1 has been subtracted from all keep in mind

    # Now each pixel contains sum of the window. But we want the average value.
    imageI = imageI/(m*n)

    # Return matrix in the original type class.
    #image = cast(imageI, class(image))     				
    print type(imageI)
    return imageI
