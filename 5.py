#Accept the name and check it is palindrome
#S = input("Enter the Name:")
#S == S.lower()
#if S == S[::-1]:
   # print(S,"is a palindrome")
#else:
   # print(S,"is not a palindrome")

S=input("Enter the Name:")
name = S[::-1]  
if S==name:
    print("it is a palindrome")
else:
    print("it is not a palindrome")

