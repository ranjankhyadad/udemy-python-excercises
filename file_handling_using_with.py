with open("Random.txt") as myfile:
    content= myfile.read()
    # myfile.close() /---not required as with uses close by itself
    print(content)