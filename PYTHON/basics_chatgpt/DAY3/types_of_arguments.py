"""
POSITINAL ARGUMENTS
add(2, 3)

KEYWORD ARGUMENTS
add(a=2, b=3)

DEFAULT ARGUMENTS
def func(a, b=10):

VARIABLE LENGTH ARGUMENTS
def func(*args):
    print(args)


"""
def func(a, b=2, c=3):
    print(a, b, c)

func(5, c=10)