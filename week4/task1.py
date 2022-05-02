# exercise 1
my_dict = {
    'key1': 0, 
    'key2': 20
}

print("exercise 1: ")
print(my_dict)
print()

# exercise 2
my_dict2 = dict([('key1', 10), ('key2', 30)])

print("exercise 2: ")
print(my_dict2)
print()


# exercise 3
nested_dict = {
    'dict1': {
        'key1': 1,
        'key2': 90
    },
    'dict2': {
        'key1': 45,
        'key2': 7
    }
}

print("exercise 3 (nested dictionary): ")
print(nested_dict)
print()

# exercise 4
new_dict = dict()
print("exercise 4 (new empty dict): ")
print(new_dict)

new_dict["key777"] = "hi"
print("exercise 4 (adding element to empty dict): ")
print(new_dict)

new_dict.update([('key1', 'hello'), ('key2', 'world!')])
print("exercise 4 (adding element via update): ")
print(new_dict)
print()


# exercise 5
print("exercise 5 (accessing element): ")
print(new_dict.get('key777'))
print()


# exercise 6
print("exercise 6 (accessing element from nested dict): ")
print(nested_dict.get('dict1'))
print("    getting key2 value from the dict returned above: ")
print(nested_dict.get('dict1').get('key2'))
print()


# exercise 7
print("exercise 7 (removing element from nested dict): ")
print("  before: ")
print(nested_dict)
print("  after: ")
del nested_dict["dict1"]
print(nested_dict)
print()

# using del to delete entire dict:
del my_dict

print("using pop to delete entire dict: ")
print("  before: ")
print(my_dict2)
my_dict2.pop('key1')
my_dict2.pop('key2')
print("  after: ")
print(my_dict2)
print()

print("using clear to delete entire dict: ")
print("  before: ")
print(new_dict)
new_dict.clear()
print("  after: ")
print(new_dict)
print()

