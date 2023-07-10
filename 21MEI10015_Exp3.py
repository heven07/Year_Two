def prt(b, a, adMat):
    print("\t",end='')
    for i in range(b):
        print("R["+str(i)+"]\t", end='')
    print()
    for i in range(a):
        print("P[" + str(i) + "]:\t", end='')
        for j in range(b):
            print(adMat[i][j], "\t", end='')
        print()
    print()
a = int(input("Processes: "))
b = int(input("Resources: "))
adMat = [[0 for i in range(b)] for j in range(a)]
print("Processes and Resources\n")
prt(b, a, adMat)
inst = [0 for j in range(b)]
for i in range(b):
    inst[i] = input("Instance for R["+str(i)+"]: ")
adList = [[] for j in range(a)]
cases = int(input("\nCase: "))
for i in range(cases):
    x = int(input("Process: "))
    y = int(input("Resource: "))
    adMat[x][y] = 1
    adList[x].append(y)
print("Adjacency Matrix\n")
prt(b, a, adMat)
print("Adjacency List\n")
for i,v in enumerate(adList):
    print("P[" + str(i) + "]: ", v)