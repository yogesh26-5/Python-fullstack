a=10
b=6
print("******Arithemetic operators****")
print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a**b)
print(a%b)
print(a//b)
print(pow(a,b))
print("*****Comparision operators*****")
print(a<b)
print(a>b)
print(a==b)
print(a!=b)
print(a<=b)
print(a>=b)
print("*****Logical operators******")
print(a and b)
print(not a)
print(a or b)
print("****BItWise operators****")
print(a & b)
print(a | b)
print(a^b)
print(~a)
print("***Shift operators****")
print(a<<b)
print(a>>b)
print("**unique element using comprehension**")
arr=[1,4,2,2,3,3]
print([item for item in arr if arr.count(item)==1])
print("Instead of switch , we use match in python")
value = 2
match value:
    case 1:
        print("One")
    case 2:
        print("Two")
    case 3:
        print("Three")
    case _:
        print("Other")
for i in range(10,0,-1):
    print(i,end=",")
print("")
for i in range(10,0,-2):
    print(i,end=",")
    break;
print("using while loops")
print("patterns")
arr[i][j]=0
for i in range(0,5):
    for j in range(0,5):
        print("*",arr[i][j])
    print(" ")
