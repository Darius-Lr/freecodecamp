import array

import numpy as np

def calculate(list):

    if len(list) != 9:
        raise ValueError("List must contain nine numbers.")



    array=np.array(list).reshape(3,3)
    calculations={}
    mean1=np.mean(array,axis=0).tolist()
    mean2=np.mean(array,axis=1).tolist()

    mean=[mean1,mean2]
    mean.append(np.mean(array).item())

    calculations["mean"]=mean
    variance1=np.var(array,axis=0).tolist()
    variance2=np.var(array,axis=1).tolist()

    variance=[variance1,variance2]
    variance.append(np.var(array).item())
    calculations["variance"]=variance
    standard1=np.std(array,axis=0).tolist()
    standard2=np.std(array,axis=1).tolist()
    standard=[standard1,standard2]
    standard.append(np.std(array).item())
    calculations["standard deviation"]=standard
    maximum1=np.max(array,axis=0).tolist()
    maximum2=np.max(array,axis=1).tolist()
    maximum=[maximum1,maximum2]
    maximum.append(np.max(array).item())
    calculations["max"]=maximum
    minimum1=np.min(array,axis=0).tolist()
    minimum2=np.min(array,axis=1).tolist()
    minimum=[minimum1,minimum2]
    minimum.append(np.min(array).item())
    calculations["min"]=minimum
    summation1=np.sum(array,axis=0).tolist()
    summation2=np.sum(array,axis=1).tolist()
    summation=[summation1,summation2]
    summation.append(np.sum(array).item())
    calculations["sum"]=summation



    return calculations
#print(calculate([2,6,2,8,4,0,1,5,7]))