n= int(input("please enter n::"))
m=int(input("please enter m::"))
for t in range(n):
    if t%2!=0:
        for p in range(m):
            print("*#",end="")
    else:
        for p in range(m):
            print("#*",end="")
    print()