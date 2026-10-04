string1 = "Hello "
name = input("Enter your Name: ")

string2 = string1 + name
print(string2)

string3 = ", welcome to Python programming"
string2 = string2 + string3

print(string2)
# Question 2

string = "Hello Rusaina, welcome to Python programming"

# a. First character
print(string[0])

# b. Last character
print(string[-1])

# c. First 5 characters
print(string[:5])

# d. Last 11 characters
print(string[-11:])

# e. Reverse the string
print(string[::-1])

# f. Print Python
print(string[23:29])

strM = "Python beginner tutorial"

# a. Convert to uppercase
print(strM.upper())

# b. Convert to lowercase
print(strM.lower())

# c. Capitalize
print(strM.capitalize())

# d. Count the character 't'
print(strM.count('t'))

# e. Replace Python with Machine Learning
print(strM.replace("Python", "Machine Learning"))

tuple1 = (10, 20, 30)
tuple2 = (40, 50, 60)

# a. Concatenate the two tuples
t_combine = tuple1 + tuple2
print(t_combine)

# b. Repeat t_combine 3 times
print(t_combine * 3)

# c. Access the 3rd element
print(t_combine[2])

# d. Access the first three elements
print(t_combine[:3])

# e. Access the last three elements
print(t_combine[-3:])