from submodule.test_math import test_add

def testing_submodule(a:int,b:int):
    c = test_add(a,b)
    print(c)

if __name__ == '__main__':
    testing_submodule(1,2)
