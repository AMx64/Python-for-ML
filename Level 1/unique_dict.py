testcase = [("Alice", 40), ("Bob", 50), ("Alice", 70), ("Bob", 30)]

def unique_dict(name_age_list):
    name_age_dict = dict()
    for name_age in name_age_list:
        name, age = name_age
        if name not in name_age_dict or age > name_age_dict[name]:
            name_age_dict[name] = max(age, name_age_dict.get(name, 0))
    print((name_age_dict))

unique_dict(testcase)
            