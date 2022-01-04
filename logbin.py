import math as math
import numpy as np


def log_bin(dict,n_bins):
    
    # first we need to define the interval of dict values
    
    min_val=sorted(dict.values())[0]
    max_val=sorted(dict.values())[-1]
    delta=(math.log(float(max_val))-math.log(float(min_val)))/n_bins
    
    # then we create the bins, in this case the log of the bins is equally spaced (bins size increases exponentially)
    
    bins=np.zeros(n_bins+1,float)
    bins[0]=min_val
    for i in range(1,n_bins+1):
        bins[i]=bins[i-1]*math.exp(delta)
        
    
    # then we need to assign the dict of each node to a bin
        
    values_in_bin=np.zeros(n_bins+1,float)
    nodes_in_bin=np.zeros(n_bins+1,float)  # this vector is crucial to evalute how many nodes are inside each bin
        
    for i in dict:
        for j in range(1,n_bins+1):
            if j<n_bins:
                if dict[i]<bins[j]:
                    values_in_bin[j]+=dict[i]
                    nodes_in_bin[j]+=1.
                    break
            else:
                if dict[i]<=bins[j]:
                    values_in_bin[j]+=dict[i]
                    nodes_in_bin[j]+=1.
                    break
    
    
    # then we need to evalutate the average x value in each bin
    
    for i in range(1,n_bins+1):
        if nodes_in_bin[i]>0:
            values_in_bin[i]=values_in_bin[i]/nodes_in_bin[i]
            
    # finally we get the binned distribution        
            
    binned=[]
    for i in range(1,n_bins+1):
        if nodes_in_bin[i]>0:
                x=values_in_bin[i]
                y=nodes_in_bin[i]/((bins[i]-bins[i-1])*len(dict))
                binned.append([x,y])
    return binned
