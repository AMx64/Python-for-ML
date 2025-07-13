from functools import reduce

testcase = list(map(int, input().split()))

def reduce_product(lst):
    prod_lst = reduce(lambda x, y: x*y, lst)
    print(prod_lst)

reduce_product(testcase)