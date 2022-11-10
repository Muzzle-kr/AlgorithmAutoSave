alphabet = input()
count = 0

count += alphabet.count('dz=')
alphabet = alphabet.replace('dz=', '^')

count += alphabet.count('z=')
alphabet = alphabet.replace('z=', '^')

count += alphabet.count('lj')
alphabet = alphabet.replace('lj', '^')

count += alphabet.count('nj')
alphabet = alphabet.replace('nj', '^')

count += alphabet.count('c-')
alphabet = alphabet.replace('c-', '^')

count += alphabet.count('d-')
alphabet = alphabet.replace('d-', '^')

count += alphabet.count('nj')
alphabet = alphabet.replace('nj', '^')

count += alphabet.count('c-')
alphabet = alphabet.replace('c-', '^')

count += alphabet.count('c=')
alphabet = alphabet.replace('c=', '^')

count += alphabet.count('s=')
alphabet = alphabet.replace('s=', '^')

minusCount = alphabet.count('^')
count += len(alphabet) - minusCount
print(count)