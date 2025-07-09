a=int(input())
for i in range(a):
    for j in range(i+1):
        print("*",end=" ")
    print()

for i in range(5):
    for j in range(i-1):
        print("*",end=" ")
    print()

import  math
print(math.gcd(6,9))