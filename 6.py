#print the sum of digits
# Accept a number from user
num = int(input("Enter a number: "))

# Initialize sum
sum = 0

# Loop to extract digits
while num > 0:
    digit = num % 10       # last digit
    sum  += digit    # add to sum
    num = num // 10        # remove last digit

print("Sum of digits:", sum)