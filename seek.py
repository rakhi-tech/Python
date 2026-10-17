with open("sample.txt","r") as f:
   f.seek(9)
   data = f.read(5)
   print(data)
