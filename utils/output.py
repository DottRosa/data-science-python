def printhash(d, indent=0):
    for key, value in d.items():
        print('\t' * indent + str(key))
        if isinstance(value, dict):
            printhash(value, indent + 1)
        else:
            print('\t' * (indent + 1) + str(value))


def printlist(list):
    for item in list:
        print(item)
