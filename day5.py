a= list(range(1, 10))
print(a)
a.append(11)
print("After adding : ",a)
a.pop(0)
print("After removing : ",a)
max=max(a)
print("Maximum in the list : ",max)
min=min(a)
print("Minimum in the list : ",min)


def Reverse(tuples):
    new_tup = tuples[::-1]
    return new_tup
tuple= ("a","b","c","d")
print(Reverse(tuple))


Tuple = ("cherry", "banana", "apple", "papaya")
List = list(Tuple)
print ("List elements : ", List)
