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
        
        acu=(lambda vvv:vvv+f"{c}, ")(acu)
        
        if((lambda vvv2:vvv2>2)(i)):
            a=b
            b=c            
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
        acu=(lambda vvv:vvv+f"{fiboAuxRecursivo(i)}, ")(acu)
    return acu

def serieFibo(funcion, x):
    return funcion(x)        

print("Serie fibonacci \n")
print("Estructurada\n")

print(serieFibo(fiboEstructurado,11))

print("\n")
print("Recursiva\n")
print(serieFibo(fiboRecursivo,11))