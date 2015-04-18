import cv2
from avgfilter import averagefilter
import numpy as np

def nick(file,*argvs):	

    x=cv2.imread(file)
    image=cv2.cvtColor(x,cv2.COLOR_BGR2GRAY)
    argv=[]
    for r in argvs:
        argv.append(r)
    num=len(argv)    	
    if num>3:
        print('image [m n] threshold padding')
        return

    optargs=[[15,15], -0.2, 'edge']  
    print argv
    print num
    optargs[0:num] = argv
    print optargs
    window, k, padding = optargs[:]


    # Convert to double
    image=image.astype(float)

    # Mean value
    mean = averagefilter(image, window, padding)

    # Standard deviation
    meanSquare = averagefilter(image**2, window, padding) 
    variance = meanSquare - mean**2

    # Nick
    threshold = mean + k*np.sqrt(variance + mean**2)
    output = image > threshold   
    output=output.astype(int)      			
    print threshold
    return output
