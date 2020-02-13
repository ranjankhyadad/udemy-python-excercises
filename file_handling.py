myfile= open("Random.txt")
content= myfile.read()
myfile.close()
print(content[:21])