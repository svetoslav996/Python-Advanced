def concatenate(*args):
    result = ''
    for word in args:
        result += word
    return result


print(concatenate("Soft", "Uni", "Is", "Great", "!"))
print(concatenate("I", " ", "Love", " ", "Python"))