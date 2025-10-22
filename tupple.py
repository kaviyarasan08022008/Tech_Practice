#Tupple:

#1
length = len(fruits)
print("1. Length of tuple:", length)

# 2 
index_banana = fruits.index("banana")
print("2. First occurrence of 'banana' is at index:", index_banana)

# 3 
try:
    fruits[2] = "grape"
except TypeError as e:
    print("3. Error:", e)
    print("   Explanation: Tuples are immutable, meaning their elements cannot be changed after creation.")

# 4. T
fruits_list = list(fruits) 
fruits_list[2] = "grape"   
fruits = tuple(fruits_list) 
print("4. Modified tuple:", fruits)


