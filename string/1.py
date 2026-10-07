text = "Wlcome to imcc!"
print("Remove the spaces",text.strip())#strip the spaces from both ends
print("lower case:",text.lower())
print("upper case:",text.upper())
print("capitalize the first leeter:",text.capitalize())
#tittle case (capitalize the each word)
print(text.title())
print(" letter c occurs:",text.count("c"),"times in text")
#find the position of a sunstring(-1 if not found)
print("Position of imcc in text is ",text.find("imcc"))
#replace a substring
print(text.replace("imcc","pyhton is magic"))

#check if string starts or end s
# with certain sunstring
print(text.startswith("we"))
print(text.endswith("!"))
#split string inot list by a delimeter
print("simple spilt",text.split())
#join the list of stringd with a seperator
words = ["python","is","fun"]
print(" ".join(words))