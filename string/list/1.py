#empty list 
list = []
print(list)
fruits = ["apple","banana","cherry"]
print(fruits)
#to acces list element use index
#positive numbers indicst from th start negative numbers 



#Append item in list 
color =["red"]
color.append("green")
print(color)

#insert at specific location
#




#function # lenghh
num = [1,2,3,4,5,6,7,8]
print(len(num))
#sum
print(sum(num))
#sorting
print(sorted(num))
print(sorted(num,reverse=True))
#display sum of last 4 elements and remove the 2 and 5 fifth position elements and print the diiference of highest and smallest of number of list and append a new elemnt in alist which is half of the item of third position in the list
Numbers = [1,2,3,4,5,6,7,8,9,10]
print(sum(Numbers[-4:]))
#removing the elements from the specific position
Numbers.remove(2)
Numbers.remove(5)
print(Numbers)
#difference between highest and lowest number
highest = max(Numbers)
lowest = min(Numbers)
diff = highest - lowest
print(diff)
#appending the element in the list
Numbers.append(Numbers[3]/2)
print(Numbers)
