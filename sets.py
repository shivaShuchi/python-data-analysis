# empty_set = {}
empty_set = set()
print(type(empty_set))
print(empty_set)

num_set = {10,20,30}
print(num_set)

text_set = {"ishq", "monica", "gehra"}
print(text_set)

mixed_set = {101,"erica",70.5,True,(11,12,13)} # only hashable elements(immutable elements) allowed
print(mixed_set)

# duplicates not allowed
num_set = {10,20,30,30,20}
print(num_set)


# operations
print(len(num_set))
print(max(num_set))
print(min(num_set))
# NO INDEXING
# NO SLICING
# NO CONCATENATION
# NO REPLICATION
