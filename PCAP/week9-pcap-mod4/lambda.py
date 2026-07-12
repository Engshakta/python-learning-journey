# syntax  lambda arguments : expressision
print((lambda x: x * x)(5))

mulitplier = lambda a,b : a * b
print(mulitplier(3,4))

transform = lambda x : x ** 2
result = [transform(num) for num in range(4) if num % 2 !=0]
print(result)
