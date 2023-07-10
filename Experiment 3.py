def contiguousFST():
    sdisk=int(input("Enter size of disk needed: "))
    arr=[]
    for i in range(sdisk):
        arr.append(0)
    print(arr)
    nofiles=int(input("How many number of files would you like to create: "))
    fdict={}#dictionary to store file names and sizes
    ftotsize=0
    for i in range(nofiles):
        fname=str(input("Enter file name: "))
        fsize=int(input("Enter size of file: "))
        ftotsize+=fsize
        print(ftotsize)
        if ftotsize>len(arr):
            print("File size is greater than size of disk.")
            exit()
        fdict.update({fname: fsize})
    print(fdict)
    printf=str(input("Which file would you like to be deleted"))


contiguousFST()