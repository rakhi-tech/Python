with open("sample.txt","r") as f:
    lines = f.read()
with open("reverse.txt","w") as f:
    f.writelines(lines[::-1])
print("file is successfully reversed")

