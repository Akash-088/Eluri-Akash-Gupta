# a=int(input("Enter a number: "))
# count=a if a%2!=0 else a-1

# res=[]
# for i in range(count):
#     res.append(2*i+1)

# print(", ".join(map(str,res)))


a=3
count=a if a%2!=0 else a-1
res=[]
for i in range(a):
    res.append(2*i+1)

print(", ".join(map(str,res)))

# a=4
# count=a if a%2!=0 else a-1
# res=[]
# for i in range(count):
#     res.append(2*i+1)

# print(", ".join(map(str,res)))