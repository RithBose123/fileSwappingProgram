def swapFileData():
    fileName1=input("File to swap= ")
    fileName2=input("File to swap with = ")
    with open(fileName1,"r") as a:
        data_a=a.read()
    
    with open(fileName2,"r") as a:
        data_b=a.read()
   
    
    with open(fileName1,"w") as a:
        a.write(data_b)
    with open(fileName2,"w") as b:
        b.write(data_a)
    print("data swapped")
swapFileData()