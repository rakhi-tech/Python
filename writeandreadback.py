with open("sample.txt","w") as f:
    f.write("welcome to the magical world of python")
with open ("sample.txt","r") as f:

    data= f.read()
    print(data)