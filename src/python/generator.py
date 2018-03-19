
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
    
#
# every word's start index in string
def index_words_iter(text):
    if text:
        yield 0
    for index, letter in enumerate(text):
        if letter == ' ':
            yield index + 1

result = list(index_words_iter('Four score ad server years ago...'))
print(result)
