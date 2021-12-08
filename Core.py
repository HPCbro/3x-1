f = open("dfsdfsfddf.txt",'w')
m = int(input("min:"))
n = int(input("max:"))
x = 0
for x in range(m,n):
    print(str(x)+"/"+str(n))
    f.write("start:"+str(x)+"\n")
    while x > 1:
        if x % 2 == 0:
            x = x/2
            f.write(str(x)+"\n")
        else:
            x = x * 3 + 1
            f.write(str(x)+"\n")
print("The end)")
