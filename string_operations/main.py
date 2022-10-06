#addition
print('''Hello, + World''')

#multiplication
print('Hey!' * 5)
print(5 * ':)')

#checking membership
print('DFG' in 'ABCDFG')
print('XYZ' in 'ABCDFG')

#comparization
print('Me' == 'me')

#indexation
letters = 'ABCDEFG'
print(letters[0])
print(letters[-3])

#slicing
letters= 'ABCDEFG'
print(letters[3:5])
print(letters[1:4:])

#checking length
sentence = 'The length of the sentence is:'
print(sentence, len(sentence))

#interpolation
print(f'Let\'s see... {sentence}', len(sentence))

#conversion
print(chr(1))
print(ord('#'))
print(str(49.2), str(3+29), str(3+4j))

print(int('1'))
print(float(2), float('3.8'))
print(str(3))