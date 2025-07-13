testcase = list(map(int, input().split()))

def sum_arg(*args):
    sum_all = sum(args)
    print(sum_all)

sum_arg(*testcase)