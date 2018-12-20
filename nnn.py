result=""
for r in range(7):
    for c in range(6):
        if (((c==0 or c==4) and r!=0) or ((c>0 and c<4 ) and (r==0 or r==3))):
            result += "* "
        else:
            result += "  "
    result += "\n"
print(result)
print("===========================")
print("T pattren")
result=""
for r in range(5):
    for c in range(4):
        if (c==3 or r==0):
                result+="* "
        else:

            result+=" "
    result+="\n"
print(result)
print("============0=================")
print("o pattren")
result=""
for r in range(7):
    for c in range(5):
        if (((c==0 or c==4) and (c!=0 or c!=7)) or (r==0 or r==6)) :
            result += "*"
        else:

         result += " "
    result += "\n"
print(result)

print("=================================")
print("D pattren")
result=""
for r in range(7):
    for c in range(5):
        if (c==0  or ((r==0 or r==6)) and ((c>0 and c<4)) or (c==4 and (r!=0 and r!=6))) :
            result +="*"
        else:
            result +=" "
    result +="\n"
print(result)

print("===========================")
print("P pattren")
for r in range(7):
    for c in range(5):
        if ((c==0 or (r==3 or r==0) and c>0 and c<4) or (c==4 and (r==1 or r==2))) :
            print("* ",end="")
        else:
            print(end="  ")
    print("")
print("================================")
print("R pattren")

for r in range(7):
    for c in range(5):
        if ((c==0 or (r==3 or r==0) and c>0 and c<4) or ((c==4 and (r!=0 and r<3 ) or (c==r-2 and r>2)))):
            print("* ",end="")
        else:
            print(end="  ")
    print("")

print("=================================")
print("E  pattren")
for r in range(7):
    for c in range(5):
        if (c==0 or (r==0 or r==3 or r==6)):
            print("* ",end="")
        else:
            print(" ",end="")
    print("")
print("===========================")
print("G pattren")
for r in range(7):
    for c in range(5):
        if (c==0 and(r!=0 and r!=6) or ((c>0 and c<4 ) and (r==0 or r==6))or (r==3 and(c>1)) or (c==4 and  (r!=0 and r!=2 and r!=6))):
            print("*",end="")
        else:
            print(" ",end="")
    print("")
print("=================================")
print("L pattren")
for r in range(7):
    for c in range(5):
        if (c==0 or r==6):
            print("* ",end="")
        else:
            print(end="")
    print("")
print("======================================")
print("Q pattren ")
for r in range(7):
    for c in range(7):
        if (c==0 or c==4 or r==4 or r==0 ) and ( r!=5 and r!=6  and c!=5 and c!=6)  or ( c==r-0 and r>4) :
            print("*",end="")
        else:
            print(end=" ")
    print("")
print("=============================================")
print("M pattren")
for r in range(7):
    for c in range(5):
        if (c==0 or c==4) or (r==2 and c!=2) or (r==3 and c!=1 and c!=3):
            print("*",end="")
        else:
            print(end=" ")
    print("")
print("=========================================")
print("U pattren")
for r in range(6):
    for c in range(5):
        if (((c==0 or c==4) and r!=5) or (r==5 and c!=0 and c!=4)):
            print("*",end="")
        else:
            print("",end=" ")
    print("")
print("==================================")
print("X pattren")
for r in range(5):
    for c in range(4):
        if ((c==0 or c==3) and (r!=1 and r!=2 and r!=3)) or ( r==1 and (c!=0 and c!=3 ) or (r==2 and (c!=0 and c!=1 and c!=3) or ( r==3 and (c!=0 and c!=3 )))):
            print("*",end=" ")
        else:
            print(end=" ")
    print("")
print("=================================")
print("Z pattren")
for r in range(5):
    for c in range(4):
        if (r==0 or r==4):
            print("* ",end="")
        else:
            print(end="")
    print("")