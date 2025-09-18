def cumsum(x):
    if x < 1: 
        return 0
    else: 
        return x + cumsum(x-1)
    
print (cumsum(3))