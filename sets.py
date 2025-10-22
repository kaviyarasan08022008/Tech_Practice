# Given set
rainfall_data = {100, 120, 150, 110, 130, 140}

# 1
print("1. Number of rainfall values:", len(rainfall_data))

# 2
try:
    rainfall_data[0] = 200
except TypeError as e:
    print("2. Error:", e)
    print("   Explanation: Sets are unordered and unindexed, so you can’t change values by index.")
# 3.
try:
        rainfall_data[0] = 200
except TypeError as e:
        print("Error:", e)
        print("Explanation: Sets are unordered and unindexed, so you cannot change a value using its index.")
# 4
print("3. Is 150 in rainfall_data?", 150 in rainfall_data)

# 5
rainfall_list = list(rainfall_data)
print("4. Converted list:", rainfall_list)

# 6
print("5. Rainfall values:")
for value in rainfall_data:
    print(value)

# 7
rainfall_data.remove(120)
print("6. After removing 120:", rainfall_data)

# 8
rainfall_data.add(110)
print("7. After adding 110:", rainfall_data)
print("   Explanation: 110 does not appear twice because sets do not allow duplicate values.")

