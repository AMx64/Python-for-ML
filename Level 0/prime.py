testcase = list(map(int, input().split()))

def sieve_of_eratosthenes(n):
    if n < 2:
        print("No Primes")
        return
    if n == 2:
        print([2])
        return
    arr = [True] * ((n - 1) // 2)
    for i in range(int(n**0.5 - 1) // 2 + 1):
        if arr[i]:
            num = 2 * i + 3
            start = (num * num - 3) // 2
            for j in range(start, ((n - 1) // 2), num):
                arr[j] = False

    ans = [2]
    for i in range(((n - 1) // 2)):
        if arr[i]:
            ans.append(2 * i + 3)

    print(ans)

for case in testcase:
    sieve_of_eratosthenes(case)
