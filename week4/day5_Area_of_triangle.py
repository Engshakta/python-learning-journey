def is_trangle(a,b,c):
    if a + b <= c:
        return False
    if b + c <= a:
        return False
    if c + a <= b:
        return False
    
    return True


result = is_trangle(2,2,10)
print(result)



def waa_saddex_xagal(x, y, z):
    if x + y > z and \
       y + z > x and \
       z + x > y :
        return True


def is_even(number):
    if number % 2 == 0:
        return True
    else :
        return False
print(is_even(10))


def is_a_triangle(a,b,c):
    return a + b > c and b + c > a and \
    c + a > b

def heron(a,b,c):
    p = (a + b + c) / 2
    return (p * (p -a) * (p-b) * (p-c)) ** 0.5

def area_of_triangle(a,b,c):
    if not is_a_triangle(a, b,c):
        return None
    return heron(a,b,c)

print(area_of_triangle(1. , 1. , 2. ** .5))


def is_a_right_triangle(a,b,c):
    if not is_a_triangle(a,b,c):
        return False
    if c > a and c > b:
        return c ** 2  == a **2 + b ** 2
    if a > b and a > c: 
        return a ** 2 == b ** 2 + c ** 2
    
print(is_a_right_triangle(5,4,3))
print(is_a_right_triangle(1,3,4))

    

a = float(input("Enter First side\'s length: "))
b = float(input("Enter Second side\'s length: "))
c = float(input("Enter Third side\'s length: "))

if is_a_triangle(a,b,c):
    print("Yes, it can be a trinagle.")
else:
    print("No, it can\'t be trinagle")


def factorial_function(n):
    if n < 0:
        return None
    if n < 2:
        return 1
    return n * factorial_function(n-1)

print(factorial_function(10))

def fib(n):
    if n < 1:
        return None
    if n < 3 :
        return 1
    return fib(n - 1) + fib(n - 2)
  
print(fib(10))


def factorial(n):
    if n == 1:    # The base case (termination condition.)
        return 1
    else:
        return n * factorial(n - 1)


print(factorial(4)) 


print(dir(list))
