numbers = {10, 20, 30}
print(numbers)

numbers.add(40)
print(numbers)

numbers.update((50, 60, 70))
print(numbers)

numbers.remove(70)
print(numbers)
numbers.discard(60)
print(numbers)
# numbers.remove(100) # if element not found, KeyError
numbers.discard(100) # if element not found, no error
# numbers.clear()
# print(numbers)

numbers_backup = numbers.copy()
print(numbers_backup)

# union(|) intersection(&)
