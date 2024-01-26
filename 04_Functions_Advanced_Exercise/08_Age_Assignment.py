def age_assignment(*args, **kwargs):
    result = {}
    for name in args:
        first_letter = name[0]
        age = kwargs[first_letter]
        result[name] = age

    return result


print(age_assignment("Peter", "George", G=26, P=19))