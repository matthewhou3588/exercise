
# generator method 1
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a+b
        n = n + 1

for n in fib(6):
    print(n)

# generator method 2
gener = (x**2 for x in range(5))
for r in gener:
    print(r)
