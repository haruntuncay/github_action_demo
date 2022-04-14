from obj import MyClass

def increment(n=1):  
    return n + 1
     
def multiply(n=1, m=10):
    return n * m

def mysum(arr):
    return sum(arr)
    
def object_test(obj1, obj2):
    obj3 = MyClass(obj1.x, obj2.y)
    return obj3.x + obj3.y
