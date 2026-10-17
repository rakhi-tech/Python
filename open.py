f = open("sample.txt","r")
data = f.read()

line1 = f.readline()
print(line1)
line2 = f.readline()
print(line2)
f.close()