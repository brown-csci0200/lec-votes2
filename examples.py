####################################
# Dictionaries: Python's version of the Java HashMap

some_dict = {"a": 1, "b": 2, "c": [1, 2, 3, 4]}

# Dictionaries can have comprehensions just like lists can
other_dict = {"a": 0, "b": 0, "c": 0, "d": 0}
options = ["a", "b", "c", "d"]
other_dict2 = {x: 0 for x in options}
print(other_dict2)


####################################
# List comprehensions: a way to process stuff in lists quickly

# Have this
ex1 = ["8", "10", "-5.5"]

# Want: [8, 10, 5.5]
result1 = [float(x) for x in ex1]

####################################
# Have this
ex2 = ["hello", "WORLD", "pYthon"]

# Want: ["hello", "world", "python"]
result2 = [float(s) for s in ex2]

####################################
# Have this
ex3 = [0, 5, -2, -4, 7]

# Want: [5, 7]
result3 = [x for x in ex3 if x > 0]

####################################
# Have this
ex4 = ["pvd", "boston", "wos", "newport"]

# Want: ["PVD", "WOS"]
result4 = [word.upper() for word in ex4 if len(word) <= 3]

####################################
# Have this
# Indices:  0, 1, 2, 3, 4, 5
ex5 =      [8, 3, 5, 9, 0, 2]

# Want: [0, 4, 5]  (indices of the even numbers)
# enumerate produces pairs (i, n) where i is the index of the element and n is the element itself
result5 = [index for (index, n) in enumerate(ex5) if n % 2 == 0] 

####################################