import math
testcase = list(map(int, input().split()))

def armstrong(n):
    if n==0:
        print("YES")
        return
    size = math.floor(math.log10(n)) + 1
    m = n
    n_map = []
    while n > 0:
        num = n - (n//10)*10
        n_map.append(num**size)
        n //= 10
    print("YES") if m == sum(n_map) else print("NO")

for case in testcase:
    armstrong(case)
        
    