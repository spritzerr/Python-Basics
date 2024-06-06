b = [101, 5, 8, 145, 5, 67, 730, 85, 5]
print(b)

# Sum the whole list.
print(sum(b))

# Sum last 2 numbers.
print(sum(b[-2:]))

# Sum first 3 numbers.
print(sum(b[:3]))

# Sum from index 2 to index 6.
print(sum(b[2:6]))

# Sum of the number from index 3 to the end of the list.
print(sum(b[3:]))

# Calculate the range.
print(max(b)-min(b))

# Calculate max.
print(max(b))

# Calculate min.
print(min(b))

# Calculate average and round it up to 2 decimal points.
print(round(sum(b)/len(b),2))

# Count the number of times "5" is found in the list.
print(b.count(5))

# Count the number of values thar is more than 100.
counter = 0
for i in range(len(b)):
    if b[i] > 100:
        counter += 1
print(counter)

# Sum the smallest 4 values from the list.
b.sort()
print(sum(b[:4]))

# Sum the largest 4 values from the list.
b.sort()
print(sum(b[4:]))

# Remove index 2 from the list.
b.pop(2)
print(b)

# Remove the first occurence of the indicated item.
b.remove(5)
print(b)
