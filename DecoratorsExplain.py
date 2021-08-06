import time

def operatsiooniaeg(funktsioon):
    def wrapper(*args, **kwargs):
        algus = time.perf_counter()
        funktsioon(*args, **kwargs)
        print('aeg :', time.perf_counter() - algus)
    return wrapper


@operatsiooniaeg
def minu_funktsioon(a):
    sum_result = 0
    for i in range(a):
        sum_result += i
        #print(i)
    print(sum_result)


minu_funktsioon(100000)