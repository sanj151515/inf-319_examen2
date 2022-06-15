def fiboEstructurado(x):
    a=0
    b=1
    c=0
    acu=""          
    len1=range(1, x+1) 
    for i in len1:        
        if i==1: c=0
        if i==2: c=1
        if i>2: c=a+b
        
        acu=acu+f"{c}, "
        
        
        if i > 2: a=b
        else: a=0

        if i > 2: b=c
        else: b=1
    return acu
        

def fiboAuxRecursivo(x):
    if x==1: return 0
    if x==2: return 1
    if x==3: return 1
    if x>3: return fiboAuxRecursivo (x-1) + fiboAuxRecursivo (x-2)
 
def fiboRecursivo(x):
    acu=""    
    len2=range(1, x+1)
    for i in len2 :
        aux=fiboAuxRecursivo(i)
        acu=acu+f"{aux}, "
    return acu
        

print("Serie fibonacci \n")
print("Estructurada\n")
print(fiboEstructurado(11))

print("\n")
print("Recursiva\n")
print(fiboRecursivo(11))