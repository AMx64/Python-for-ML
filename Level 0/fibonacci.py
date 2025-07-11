testcase = list(map(int, input().split()))

def fibonacci(n):
    if n == 0:
        print(0)
    elif n == 1:
        print(1)
    else:
        a, b = 0, 1
        for i in range(2, n + 1): 
            a, b = b, a + b
        b = b % (10**9+7)
        print(b)

for case in testcase:
    fibonacci(case)
