def fibo(limit):
    a, b = 0, 1
    for _ in range(limit):
        yield a
        a, b = b, a + b

for num in fibo(200):
    print(str(num) + ",")