import itertools
#https://www.youtube.com/watch?v=Qu3dThVy6KQ
from collections import Counter
data = [1,2,3,4,5,6]
counter = itertools.count() #start, step


for num in counter: #Do not run -- infinite loop
    print(num)
print(next(counter))
print(next(counter))
print(list(zip(itertools.count(), data)))

print(list(itertools.zip_longest(range(10), data)))

cycle = itertools.cycle(('on', 'off'))
cycle = itertools.cycle([1,2,3])

print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))
print(next(cycle))

repeats = itertools.repeat(2, times=3)
print(next(repeats))
print(next(repeats))
print(next(repeats))

squares = map(pow, range(10), itertools.repeat(2))
print(list(squares))

squares2 = itertools.starmap(pow, list(zip(range(3), itertools.repeat(2))))
print(list(squares2))

letters = ['a', 'b', 'c', 'd']
numbers = [0,1,2,3,2,1,0]
names = ['Corey', 'Nicole']


comb = itertools.combinations(letters, 2)
for item in comb:
    print(item)

comb_with = itertools.combinations_with_replacement(numbers, 4)
for item in comb_with:
    print(item)

perm = itertools.permutations(letters,2)
for item in perm:
    print(item)

product = itertools.product(numbers, repeat=4)
for item in product:
    print(item)

productl = itertools.product(*[numbers, letters])
for item in productl:
    print(item)

combined = itertools.chain(letters, numbers, names)
 
for item in combined:
    print(item)

result_slice = itertools.islice(range(10), 5)

for item in result_slice:
    print(item)


result_slice2 = itertools.islice(range(10), 1, 5)

for item in result_slice2:
    print(item)


result_slice3 = itertools.islice(range(10), 1, 5, 2)

for item in result_slice3:
    print(item)

selectors = [True, True, False, True]
compr = itertools.compress(letters, selectors)
for item in compr:
    print(item)


def vlt_2(n):
    if n < 2:
        return True
    return False


result_t = filter(vlt_2, numbers)
for item in result_t:
    print(item)

result_f = itertools.filterfalse(vlt_2, numbers)
for item in result_f:
    print(item)

result = itertools.dropwhile(vlt_2, numbers)

for item in result:
    print(item)


result23 = itertools.takewhile(vlt_2, numbers)

for item in result23:
    print(item)

accum = itertools.accumulate(numbers)

for item in accum:
    print(item)

import operator
accum2 = itertools.accumulate(numbers, operator.mul)

for item in accum2:
    print(item)

people = [
    {
        'name': 'John Doe',
        'city': 'Gotham',
        'state': 'NY'
    },
    {
        'name': 'Jane Doe',
        'city': 'Kings Landing',
        'state': 'NY'
    },
    {
        'name': 'Corey Schafer',
        'city': 'Boulder',
        'state': 'CO'
    },
    {
        'name': 'Al Einstein',
        'city': 'Denver',
        'state': 'CO'
    },
    {
        'name': 'John Henry',
        'city': 'Hinton',
        'state': 'WV'
    },
    {
        'name': 'Randy Moss',
        'city': 'Rand',
        'state': 'WV'
    },
    {
        'name': 'Nicole K',
        'city': 'Asheville',
        'state': 'NC'
    },
    {
        'name': 'Jim Doe',
        'city': 'Charlotte',
        'state': 'NC'
    },
    {
        'name': 'Jane Taylor',
        'city': 'Faketown',
        'state': 'NC'
    }
]


def get_state(person):
    return person['state']

#Groupby expects a sorted object.
person_group = itertools.groupby(people, get_state)

for k, v in person_group:
    print(k)
    for person in v:
        print(person)
    print()

#copying an iterable
copy1, copy2 = itertools.tee(people)

