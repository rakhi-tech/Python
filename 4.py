#create the heterogeneous list of numbers and names .split the list of highest number

data = [10, "Rakhi", 25, "Amit", 5, "Sneha", 40, "Vikas"]


highest = None
for item in data:
    if isinstance(item, int):   
        if highest is None or item > highest:
            highest = item


first_part = []
second_part = []
found = False

for item in data:
    if item == highest:
        found = True  
        continue       
    if not found:
        first_part.append(item)
    else:
        second_part.append(item)

print("Highest number:", highest)
print("First part:", first_part)
print("Second part:", second_part)




