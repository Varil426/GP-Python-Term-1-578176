dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Łączenie słowników - Python 3.5+
dict3 = {**dict1, **dict2}
print(dict3)

# Łączenie słowników - Python 3.9+
dict4 = dict1 | dict2
print(dict4)