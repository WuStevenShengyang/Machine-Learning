import math
from data import self, others

def recommand(people, other):
    
    sum_of_squares = sum([pow(people[index] - other[index], 2) for index in people])

    return 1/(1+math.sqrt(sum_of_squares))


def compare_between(self, others):
    
    result = {}

    for name in others:
        result[name] = recommand(self, others[name])

    return result

print(compare_between(self, others))
