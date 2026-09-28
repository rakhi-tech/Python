#write a to program to print sum of digits
num = int(input("enter a number:"))
sum = 0
while(num>0): 
    sum= sum + num%10

    num = num//10
print("sum of digits",sum)