message = "This line is written using File Io"

# To Write
with open("test.txt","w") as f:
    f.write(message)

fp = open("test.txt","w")
fp.write(message)
fp.close()

# To read a File
with open("test.txt","r") as f:
    str = f.read()
    print(str)

fr = open("test.txt","r")
fr.read()
fr.close()

# To Append
with open("test.txt","a")as f:
    f.write("\nThis is a append line")