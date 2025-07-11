testcase = list(map(int, input().split()))

def duplicate(arr):
    seen = set()
    result = []
    for num in arr:
        if num not in seen:
            seen.add(num)
            result.append(num)
    print(result)
    
duplicate(testcase)