# Lambda
SignoPeso = lambda signo:f'${signo}'
print("")
print("#### Lambda method!! ####")
print(SignoPeso(100))
print("")

#Getsizeof / generator
import sys
print("#### sized difference ####")
my_list = [i for i in range(10000)]
print("")
print(sum(my_list))
print("### size in list!! ###")
print(sys.getsizeof(my_list), "bytes")

my_gen = (i for i in range(10000))
print("")
print(sum(my_gen))
print("### size in generator!! ###")
print(sys.getsizeof(my_gen), "bytes")
print("")

# Count hashable objects with collections.counter
from collections import Counter

_list = [2,2,2,2,5,5,5,5,7,7,1,1,1,1,1,1,1]
counter = Counter(_list)
print("#### Count every items ####")
print(_list)
print(counter)
print("")

# Concat with .join()

list_of_things = ["Hello" , "my", "Potilla"]

my_string = " ".join(list_of_things)
print("#### joining things!! ####")
print(my_string)
print("")

# Extender listas

courses1 = ["History", "Science", "PE", "Language"]
courses2 = ["Python", "Assembly", "C", "Perl"]

courses1.extend(courses2)
print("#### Extender listas!! ####")
print(courses1)
print("")


# Remove - pop

courses1.remove('PE')
print("#### Remove a item 'PE'!! ####")
print(courses1)
print("")

courses1.pop()
print("#### Remove last (POP) !! ####")
print(courses1)
print("")



# Merge two Dictionaries (3.5+)

d1 = {"Name": "Florencia", "age": "13"}
d2 = {"Name": "Natalia", "City": "Talagante"}
merged_dict = {**d2, **d1}

print("#### Merging dicts!! ####")
print(merged_dict)
print("")


# Search in a list
print("#### Search 'C++' in list!! ####")
print("C++" in courses1)
print("")
