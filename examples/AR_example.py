طباعة('Hello world')
صفر factorial(n):
    إذا n==1 أو 0:
        يعود 1
    else:
        يعود factorial(n-1)* n

إذا __name__=='__main__':
    طباعة(factorial(5))
