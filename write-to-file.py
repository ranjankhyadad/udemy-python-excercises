with open("bear.txt") as firstfile:
    content= firstfile.read()
    
with open("first.txt","w") as myfinalfile:
    myfinalfile.write(content[:90])