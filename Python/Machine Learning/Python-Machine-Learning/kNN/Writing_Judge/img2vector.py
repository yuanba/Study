import numpy as np

def imgtrans(filename):
    '''
        This function try to open the file "filename"
        to read the 01 string into the numpy array

        Input :
            filename : the name of the data file
        Output :
            data : the (1,1024) shape data in numpy array.
    '''
    init = np.zeros((1,1024))    # The data will be returned.
    with open(filename , 'r') as f:
        data = f.readlines()    # Read the data Once
        for i in range(32):
            for j in range(32):
                init[0 , i * 32 + j] = int(data[i][j])
        return init
