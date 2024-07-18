print('hello world from test!')

for i in range(10):
    print(f'test {i}')

def fib(n, acc=0):
    if n == 1: return 1 + acc
    if n == 0: return 0 + acc
    return fib(n-1, fib(n-2, acc))

for i in range(10):
    print(f'fib {fib(i)}')
