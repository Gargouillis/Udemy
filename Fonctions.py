"""
def foo():
    a = 5
    print(locals())

foo()
b = 2
print(globals() == locals())
"""

"""
def foo(param):
    test = param.copy()
    test.append(4)
    print(test)

var = [1, 2, 3]
print(var)
foo(param=var)
"""

def add(a: int, b: int) -> int:
    print(a + b)

add(2, 3)