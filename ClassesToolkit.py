import math
from random import random, seed


class Ring(object):
    """An advanced circle analytic toolkit"""
    
    # flyweight design pattern suppresses
    # the instance dictionary
    __slots__ = ['diameter']
    version = '0.7' # class variable. And for version number use string
    
    def __init__(self, radius):
        self.radius = radius
    
    @property # Convert dottedaccess to method calls
    def radius(self):
        return self.diameter / 2.0
    
    @radius.setter
    def radius(self, radius):
        self.diameter = radius * 2.0
    
    """sedasi saab teha rohkem konstruktoreid erinevate parameetritega cls on vajalik 
     et ka ring klassist tehtud subklassid saaks seda meetodit kasutada"""
    @classmethod 
    def from_bbd(cls, bbd):
        """construct a circle from bounding box diagonal"""
        radius = bbd / 2.0 / math.sqrt(2.0)
        return Ring(radius)

    """Regular methods have self as first argument"""    
    def pindala(self):
        y = self.__ymbermoot()
        r = y / math.pi / 2.0
        return math.pi * r**2.0
    
    def ymbermoot(self):
        return 2.0 * math.pi * self.radius

    @staticmethod # sedasi saab teha meetodeid mida saab kutsuda välja ilma objekti loomata klassimeetod
    def angle_to_grade(nurk):
        return math.tan(math.radians(nurk)) * 100.0

    __ymbermoot = ymbermoot 

# subclassing
class rehv(Ring):
    
    def ymbermoot(self):
        return Ring.ymbermoot(self) * 1.25

    
def main():
    print ('Versioon: ', Ring.version)
    r = Ring(22)
    print ('Ring raadiusega: ', r.radius)
    print ('omab pindala: ', r.pindala())
    print ('ja ymbermootu: ', r.ymbermoot())
    print ()
    
    seed (8675309)
    n = 10000000
    ringid = [Ring(random()) for i in range(n)]  
    print ('keskmine pindala ', n , 'suvalise ringi kohta')
    avg = sum([c.pindala() for c in ringid]) / n
    print ('on %.2f' % avg)
    print ()
    
    cuts = [0.1, 0.7, 0.8]
    ringid = [Ring(r) for r in cuts]
    for ring in ringid:
        print ('raadius: ', ring.radius)
        print ('ymbermoot: ', ring.ymbermoot())
        print ('kylm pindala: ', ring.pindala())
        ring.radius *= 1.1 # Pythonis on klassi muutujad kõik avalikud 
        print ('kuum pindala: ', ring.pindala())
        print ()
        
    k = rehv(22)
    print ('rehvi raadius: ', k.radius)
    print ('pind: ', k.pindala())
    print ('parandatud ymbermoot: ', k.ymbermoot())
    print ()
    
    c = ring.from_bbd(25.1)
    print ('ring raadiusega: ', c.radius)
    print ('ja pindalaga: ', c.pindala())
    print ()


if __name__ == '__main__':
    main()