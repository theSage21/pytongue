print('Hello world')
def factorial(n):
    if n == 1 or 0:
        return 1
    else:
        return factorial(n-1) * n

if __name__ == '__main__':
    print(factorial(5))
