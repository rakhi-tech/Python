#for loop
#print("print number using the loop")
#for i in range(5):
    #print(i)
    #pass - placeholder, does nothing
    #continue - skips the current location
    #break - exits loop immediately
    #for i in range(5):
       # pass

   # for i in range(5):
      #  if i ==2:
          #  continue
       # print(i)

for i in range(5):
    if i ==2:
            break
print(i)

#loop else
print("output for the loop with else")
for i in range(3):
      print(i)
else:
      print("loop finished without the break")