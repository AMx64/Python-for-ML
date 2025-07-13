testcase = list(map(int, input().split()))

def square_map(lst):
    square_lst = list(map(lambda x: x*x, lst))
    print(square_lst)

def even_filter(lst):
    even_lst = filter(lambda x: x%2 == 0, lst)
    print(list(even_lst))

square_map(testcase)
even_filter(testcase)