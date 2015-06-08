# ZH
列印('Hello world')
def factorial(n):
    如果 n==1 或 0:
        重回 1
    else:
        重回 factorial(n-1)* n

如果 __name__=='__main__':
    列印(factorial(5))
