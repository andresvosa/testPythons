from __future__ import annotations  # Klassi enda tüübi tagastuse jaoks
# import numba
from numba import jit
from typing import List, Tuple
import matplotlib.pyplot as plt


class Collatz (object):
    """Class for dealing with Collatz series
    """
    def __init__(self, start_number: int) -> None:
        """Constructor for Collatz class without calculation
        Args:
            start_number (int): Starting number for the Collatz serie
        """
        self.col_serie: List[int] = [start_number]

    @classmethod
    def calc_init(cls, start_num: int) -> Collatz:
        """Other constructor for Collatz serie object
            Also calculates the serie
        Args:
            start_num (int): Starting number for the Collatz serie

        Returns:
            Collatz: Returns the Collatz serie type object
        """
        newcol = Collatz(start_num)
        newcol.calc_serie()
        return newcol

    @staticmethod
    @jit(nopython=True)     
    def calc_next(number: int) -> int:
        """Calculate next Collatz number from integer
            Dfined as staticmethod for using numba
        Args:
            number (int): Previous collatz number

        Returns:
            int: Next collatz number
        """ 
        # return collatz_function(number)
        if number % 2 == 0:
            return int(number / 2)
        else:
            return int((3 * number) + 1)
    
    def calc_serie(self) -> Tuple[int, List[int]]:
        """Calculates Collatz serie numbers until 1 
            Starts with first list element
        Returns:
            Tuple[int, List[int]]: Serie steps, List of Collats numbers in the serie
        """
        while not (self.col_serie[-1] == 1):
            self.col_serie.append(self.calc_next(self.col_serie[-1]))
        self.steps: int = (len(self.col_serie) - 1)
        return self.steps, self.col_serie
        

@jit(nopython=True)
def collatz_function(number: int) -> int:
    """Calculate next Collatz number from integer

    Args:
        number (int): Previous collatz number

    Returns:
        int: Next collatz number
    """    
    
    if number % 2 == 0:
        return int(number / 2)
    else:
        return int((3 * number) + 1)


def main():
    """Try to calculate Collatz number series
    """
    x, y, z = map(int, ['3', '4', '5'])
    print(f'x={x}, y={y}, z={z}')
    numbrid = tuple(map(int, ('6', '7', '8')))
    print(numbrid)
    rotated_numbers = numbrid[::-1]
    print(rotated_numbers)
    # find series of collatz number
    col_start: int = 14  # 63728127 #949
    col_number: List[int] = [col_start]
    while not col_number[-1] == 1:
        col_number.append(collatz_function(col_number[-1]))
    print(len(col_number) - 1)
    print(col_number)
    
    my_col = Collatz(12)
    serlen, serie = my_col.calc_serie()
    print(serlen, serie)

    my_col2 = Collatz.calc_init(13)
    print(my_col2.steps, my_col2.col_serie)
    
    # Plot
    fig, ax = plt.subplots(nrows=3, ncols=1)
    fig.suptitle('Collatz series')
    ax[0].plot(serie, '.-')
    ax[1].plot(my_col2.col_serie, '.-')
    ax[2].plot(col_number, '.-')
    for p in ax:
        p.set_xlim([0, 20])
        p.set_ylim([0, 60])
        p.grid()
        # p.grid(which='major')
        # p.grid(which='minor')
        # p.minorticks_on()
    plt.show()

    plt.plot(serie, '.-', color='red')
    plt.plot(my_col2.col_serie, '.-', color='green')
    plt.plot(col_number, '.-', color='blue')
    plt.grid(b=True, which='major')
    plt.minorticks_on()
    plt.grid(b=True, which='minor', alpha=0.2)
    plt.legend()
    plt.show()


if __name__ == '__main__':
    main()
