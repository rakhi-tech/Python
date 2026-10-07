num = int(input("Enter a number"))
sum = 0
n=num 
while(n>0):
    sum = sum*10+n%10
    n = n//10
    if(num==sum):
        print("it is a palindrome")