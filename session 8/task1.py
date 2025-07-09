n=int(input())
print("Using end")
for i in range(1,n+1):
    if (i!=n):
        print(i, end=',')
    else:
        print(i, end='.')

print("\nUsing sep")
for i in range(1,n+1):
    if (i!=n):
        print(i, sep=',', end=',')
    else:
        print(i, sep=',', end='.')

print("\nUsing for loops")
for i in range(1,n+1):
    if (i!=n):
      