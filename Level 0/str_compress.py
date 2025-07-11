testcase = input().split()

def str_compress(string):
    i, res, curr = 0, "", string[0]
    while i < len(string):
        count = 0
        while(i < len(string) and string[i] == curr):
            count += 1
            i += 1
        res = res + curr + str(count)
        if i < len(string):
            curr = string[i]
    print(res)

for case in testcase:
    str_compress(case)