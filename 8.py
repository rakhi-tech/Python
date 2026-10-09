#add the two numbers at third position of list and append one name in a list and spilt it

data = ["Rakhi", 34, "Om", 76, "eshwari", 56, 76, 87]


numbers = [x for x in data if isinstance(x, int)]


sum = numbers[2] + numbers[3]


data.append(sum)
data.append("Vikas")


first_part = []
second_part = []
found = False

for item in data:
    if item == sum:
        found = True
        continue
    if not found:
        first_part.append(item)
    else:
        second_part.append(item)

print("Original list:", data)
print("Sum of 3rd & 4th numbers:", sum)
print("First part:", first_part)
print("Second part:", second_part)












