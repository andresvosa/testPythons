# Python notes:
# C:\Users\EEANVOS\Documents\Python Scripts\env_01
# pip install rich

# In [15]: %save -r mysession 1-99999
# The following commands were written to file `mysession.ipy`:

# Blueprint:
# condition_if_true if condition else condition_if_false

# Example:
is_nice = True
state = "nice" if is_nice else "not nice"

# Blueprint
# lambda argument: manipulate(argument)

# Example
add = lambda x, y: x + y
print(add(3, 5))
# Output: 8

# [thing for thing in list_of_things]
doubled = [num * 2 for num in lst]

# Muutujate kirjeldamine Pythonis (annotations)
some_number: int           # variable without initial value
some_list: List[int] = []  # variable with initial value

def circumference(radius: float = 10.0) -> float:
    return 2 * math.pi * radius

def haul(item: Haulable, *vargs: PackAnimal) -> Distance:
    pass
    
