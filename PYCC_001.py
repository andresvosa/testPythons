import random as rnd
import datetime

logs = [
    {
        'type': 'Brown Cowboy Boots',
        'actions': [
            {'worker_id': 1, 'part': 'heel'},
            {'worker_id': 2, 'part': 'toe box'},
        ]
    },
    {
        'type': 'Red Woman Boots',
        'actions': [
            {'worker_id': 2, 'part': 'tongue'},
            {'worker_id': 1, 'part': 'heel'}
        ]
    }
]

def get_worker_actions(records, worker_id):
    # siia tarvis funktsiooni
    pass

def list_sum(list_of_numbers):
    return sum(set(list_of_numbers))

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))

def fibonacci_only(*args):
    ret_sum = 0
    rfib = 0
    for nr in args:
        fidx = 0
        while True:
            rfib = recur_fibo(fidx)
            if rfib == nr:
                ret_sum = ret_sum + nr
                break
            elif rfib > nr:
                break
            fidx += 1        
    return ret_sum

class Person(object):
    def __init__(self, first_name, last_name, birth_date ):
        self.first_name = first_name
        self.last_name = last_name
        self.birth_date = birth_date
    
    def full_name(self):
        return self.first_name + ' ' + self.last_name


def  main ():
    randomlist = rnd.sample(range(0, 100), 10)
    print(randomlist)
    print(list_sum(randomlist))
    print(fibonacci_only(1,2,3,4, 5,6,7,8,9,610))
    isik = Person('Andres', 'Võsa', datetime.datetime.now())
    print(isik.full_name())


if __name__ == '__main__':
    main()