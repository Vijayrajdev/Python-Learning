# Lambda function

def operation(n):
    return lambda a: a * n


doubler = operation(2)
tripler = operation(3)

print(doubler(20))
print(tripler(20))
