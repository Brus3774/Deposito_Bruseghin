#tuple
punto = (3, 4)
colore_rgb = (255, 128, 0)
informazioni_persona = ("Alice", 25, "Femmina")

punto = (3, 4)
print(punto[0]) # Output: 3
print(punto[1]) # Output: 4


#Tuple packing and unpacking
punto = 3, 4 # Tuple packing
x, y = punto # Tuple unpacking
print(x, y) # Output: 3 4

#Insiemi - Set esempi

set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
print(set1.union(set2)) # Output: {1, 2, 3, 4, 5, 6, 7, 8}
print(set1.intersection(set2)) # Output: {4, 5}
print(set1.difference(set2)) # Output: {1, 2, 3}
print(set1.symmetric_difference(set2)) # Output: {1, 2, 3, 6, 7, 8}