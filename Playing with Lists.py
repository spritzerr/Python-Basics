a = [101, 12, 302, 45, 51, 67, 730, 85, 6]
print(a)

# Extract elements from index 2 to index 5 (exclusive).
print(a[2:5])

# Extract elements from index 0 to index 6 (exclusive), with a step of 2.
print(a[0:6:2])

# Extract elements from index 3 to the end of the list.
print(a[3:])

# Extract elements from the beginning of the list to index 4 (exclusive).
print(a[:4])

# Extract the last three elements of the list.
print(a[-3:])

# Reverse the list.
a.reverse()
print(a)

# Sort the list in ascending order.
a.sort()
print(a)

# Sort the list in descending order.
a.sort(reverse=True)
print(a)