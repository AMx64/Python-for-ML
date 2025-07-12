testcase = {'a': 2, 'b': 3, 'c': 0, 'd': 4, 'e': ''}

def deep_filter_dict(dictionary):
    del_key = []
    for key_value in dictionary.items():
        key, value = key_value
        if not (value and value%2 == 0):
            del_key.append(key)
    
    for key in del_key:
        del dictionary[key]
    print(dictionary)


deep_filter_dict(testcase)
