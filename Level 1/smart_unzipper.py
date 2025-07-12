testcase = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

def unzipper(zipped_list):
    A, B, C = map(list, zip(*zipped_list))
    print(A)
    print(B)
    print(C)

unzipper(testcase)