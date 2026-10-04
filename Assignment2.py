# List Creation

age_list = [24, 25, 26, 27, 28]

name_list = ["Anu", "Meera", "Diya", "Kavya", "Sneha"]

print("Age List:", age_list)
print("Name List:", name_list)

# List Operations / Modifications

# a. Append "Yazhini" to name_list
name_list.append("Yazhini")

# b. Insert 30 at index 2 in age_list
age_list.insert(2, 30)

# c. Remove "Yazhini" from name_list
name_list.remove("Yazhini")

# d. Pop the last element from age_list
age_list.pop()

# e. Extend age_list with additional ages
age_list.extend([29, 30, 26])

# f. Sort age_list in descending order
age_list.sort(reverse=True)

# g. Find maximum, minimum and sum
max_age = max(age_list)
min_age = min(age_list)
total_age = sum(age_list)

print("Updated Age List:", age_list)
print("Updated Name List:", name_list)
print("Maximum Age:", max_age)
print("Minimum Age:", min_age)
print("Sum of Ages:", total_age)

# Accessing List Elements

# a. First element
print("First element:", name_list[0])

# b. Last element
print("Last element:", name_list[-1])

# c. Elements from index 2 to index 4
print("Elements from index 2 to 4:", name_list[2:5])

# d. Reverse order
print("Reverse order:", name_list[::-1])

# Sets

my_set = {'a', 'e', 'i', 'o', 'u', 'a', 'a', 'i'}

print("My Set:", my_set)

# Attempt to change a set element

try:
    my_set[4] = 's'
except TypeError:
    print("Error: Set elements cannot be changed using index assignment.")

    set1 = {1, 3, 5, 7, 9}

set2 = {2, 3, 5, 8, 10}

print("Set 1:", set1)
print("Set 2:", set2)

union_set = set1.union(set2)
intersection_set = set1.intersection(set2)

print("Union:", union_set)
print("Intersection:", intersection_set)

# Performance Category Program

score = float(input("Enter your score (0-10): "))

if score < 0 or score > 10:
    print("Invalid score. Please enter a score between 0 and 10.")

elif score > 7:
    print("Performance Category: Above Average")
    print("Excellent performance! Keep up the good work.")

elif score >= 4:
    print("Performance Category: Average")
    print("Good effort! Keep practicing to improve further.")

else:
    print("Performance Category: Below Average")
    print("Need to improve your performance. Consistent practice will lead to better results.")