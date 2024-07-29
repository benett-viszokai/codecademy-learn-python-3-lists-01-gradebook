last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Creating lists
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]

# Appending to a 2 dimensional list
gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])

# Modifying a 2 dimensional list
gradebook[-1][-1] = 98

# Removing an element from a 2 dimensional list
gradebook[2].remove(85)

# Appending a new element
gradebook[2].append("Pass")

# Combining lists
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
