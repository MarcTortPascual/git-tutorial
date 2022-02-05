# par: /2
#impar: 3*+
base= int(input("ef"))
r=0
def es_par():
    if base%2==0:
        return True
    else:
        return False
def es_impar():
    if base%2!=0:
        return True
    else:
        return False
while base!=1:
    if es_par:
        base=base/2
        
        print(base)
    else:
        base=base*3+1
        base=r
        print(base)
        