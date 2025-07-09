str="India is my Country"
print(str.upper())
print(str.lower())
print(str.split(" "))
print(str.replace("my","our"))
print(str[::-1])
print(str.find("my")) 
print(str.strip())

a = ""
for i in range(len(str)- 1, -1, -1):
   a += str[i]
print(a)

a=list(map(int, input().split()))
print(max(a))  
print(min(a))
print(sum(a))
print(sorted(a))
print(a[::-1])