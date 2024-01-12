import itertools

# Example usage
word = 'sample'
letters = 'plmeas'

perm = itertools.permutations(letters, 6)
for p in perm:
    if ''.join(p) == word:
        print( 'Match')
        break
    else:
        print( 'No Match')

#vs
        

from collections import Counter
def is_permutation(word, letters):
    return Counter(word) == Counter(letters)


if is_permutation(word, letters):
    print('Match')
else:
    print('No Match')

