word = "learning"
with open("demo.txt","r") as f:
  data =  f.read()
  if(data.find(word)!=-1):
    print("found")
  else:
    print("not found")