def initials(name):
    first = name[0].upper()
    last = name[name.find(' ')+1].upper()
    return f'{first}. {last}.'  

print(initials('Bilal Abou-Allal'))

def multiply(a, b):
    return a * b

print(multiply(5, 5))

