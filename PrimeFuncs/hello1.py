def isp(num):
    isp = False
    
    if num != 2:    
        for x in range(2,num):
            if num % x == 0:
                isp = False
                break
            else:
                isp = True
    else:
        isp = True
    return isp

def prime_range(num):
    for x in range(2,num):
        if isp(x):
            yield x

def prime_factors(num):
    while num > 1:
        for x in prime_range(2,num):
            if num % x == 0:
                break
            else:
                x = num
                
                
                
        num //= x
        yield x
            
            
        
    

if __name__ == "__main__":
    print(isp(10))