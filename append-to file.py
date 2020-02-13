with open("bear1.txt") as firstfile:
    content= firstfile.read()
    
with open("bear2.txt","a") as secondfile:
    secondfile.write(content)
    