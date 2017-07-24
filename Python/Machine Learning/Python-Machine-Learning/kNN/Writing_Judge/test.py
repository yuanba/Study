#!/usr/bin/python3
import kNN
import img2vector as iv
import glob
import re
import numpy as np

def main():
    path1 = glob.glob(r"/home/lantian/File/Study Coding/Python/Machine Learning/Python-Machine-Learning/kNN/Writing_Judge/thumbnail/trainingDigits/*")
    label = []
    num = len(path1)    # Get the size of the training dataset
    path2 = glob.glob(r"/home/lantian/File/Study Coding/Python/Machine Learning/Python-Machine-Learning/kNN/Writing_Judge/thumbnail/testDigits/*")
    numtest = len(path2)

    # Create the label
    for i in range(num):
        w = re.search("([0-9]{1,2})_[0-9]{1,4}\.txt" , path1[i])
        label.append(int(w.group(1)))
    label = np.array(label)

    # Create the label of the test
    labeltest = []
    for i in range(numtest):
        w = re.search("([0-9]{1,2})_[0-9]{1,4}\.txt" , path2[i])
        labeltest.append(int(w.group(1)))
    labeltest = np.array(labeltest)

    training = np.zeros((num , 1024))    # The array which save the dataset
    for i in range(num):
        training[i] = iv.imgtrans(path1[i])    # Get the data!
    
    errorcount = 0
    label.shape = num,1

    for i in range(numtest):
        test = iv.imgtrans(path2[i])
        p = kNN.knn(test , training , label , 20)
        if p != labeltest[i]:
            errorcount += 1
        print("The training test result is %s , the real result is %s" % (p , labeltest[i]))
    print("The error percentile is %s " % (errorcount * 1.0 / numtest))

if __name__ == "__main__":
    main()

