import time


def f1(funk):  #See on dekoraatorfunktsioon
    def wrapper_funktsioon(*args, **kwargs): #Kui tahame kasutada dekoreeritud funktsioonis ka argumente siis tuleb dekoraator
        print('hakkan peale')                   # funktsioon defineerida *args, **kwargs argumentidega
        funk(*args, **kwargs)
        print('korras')
    
    return wrapper_funktsioon #siia ei tohi lisada () siis tähendab see funktsiooni väljakutsumist/käivitamist

def run_time(fn):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        val = fn(*args, **kwargs) #kui me tahame saada funktsiooni tagastatud väärtust dekoraatorist
        print('Aeg: ', time.perf_counter() - start_time, 's')
        return val
        
    return wrapper

@f1
def midagi():
    print('Hello midagi')
    
@f1
def midagi_parameetriga(a):
    print(a)


def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
   
@run_time
def fibonacci(n):
    a = 0
    b = 1
     
    # Check is n is less
    # than 0
    if n < 0:
        print("Incorrect input")
         
    # Check is n is equal
    # to 0
    elif n == 0:
        return 0
       
    # Check if n is equal to 1
    elif n == 1:
        return b
    else:
        for _ in range(1, n):
            c = a + b
            a = b
            b = c
            #time.sleep(1)
        return b
#f1(midagi)()

#x = f1(midagi) #Sellise rea saab asendada dekoraatoriga 
#print(type(x))

midagi() #Dekoraator annab dekoreeritud funktsiooni edasi dekoraatorile 

midagi_parameetriga('parameeter') #argumendi kasutamisel dekoreeritud funktsioon

print(recur_fibo(25)) 

print(fibonacci(25)) #dekoreeritud funktsioon tagastatava väärtusega

