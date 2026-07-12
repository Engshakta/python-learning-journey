def dynamic_range(n):
    for i in range(n):
        yield i

result = [x * 10 for x in dynamic_range(4) if x > 1]
print(result)