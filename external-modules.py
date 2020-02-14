import time
import os
import pandas

while(True):
    if os.path.exists("data.csv"):
        data = pandas.read_csv("data.csv")
        print(data.mean())
    else:
        print("File doesn't exist")
    time.sleep(10)