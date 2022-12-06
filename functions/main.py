# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line
def greet(name):
    print(f'Hello, {name}!')

greet('Bilal')

def add(a, b, c):
    add_result = a + b + c
    print(add_result)

add(5, 5, 5)

def positive(number):
    if number > 0:
        print(True)
    else:
        print(False)

positive(5)
positive(-5)

def negative(number):
    if number < 0:
        print(True)
    else:
        print(False)

negative(5)
negative(-5)