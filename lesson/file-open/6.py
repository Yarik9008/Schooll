for i in range(10000,1,-1):
    n = 1024
    s = i
    while s >= 5:
        s = s - 5 
        n = n // 2
    if  n == 64:
        print(i)
        break
        
    
        
        
        