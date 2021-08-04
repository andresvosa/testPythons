import time

def operatsiooniaeg(funktsioon):
    def wrapper(*args, **kwargs):
        algus = time.perf_counter()
        funktsioon(*args, **kwargs)
        print('aeg :', time.perf_counter() - algus)
    return wrapper


@operatsiooniaeg
def minu_funktsioon(a):
    sum = 0
    for i in range(a):
        sum += i
        #print(i)
    print(sum)


minu_funktsioon(100000)