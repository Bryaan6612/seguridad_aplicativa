a=[8,9,10,6,6,7,8,9,5,6,7,6,8,8,9,9,5,6,7,9,10,7,8,9,9]


def promedio():
   promedio = (sum(a)/ len(a))
   print (promedio)

def reprobaron():
    r=0
    for num in a:
        if (num <= 5):
            r = r + 1
            print ("Reprobados: ", r)
            
promedio()
reprobaron()
    
