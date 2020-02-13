with open("data.txt") as myfile:
    content=myfile.read()
    
with open("data.txt","a") as myfile1:
    myfile1.write(content)
    myfile1.write(content)