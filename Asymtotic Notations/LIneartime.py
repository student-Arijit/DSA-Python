n = int(input("n = "))
k = int(input("k = "))
for i in range(n): #O(n)
    print(i, end=" ") 
print("\n")

for i in range(n+100): #O(n)
    print(i, end=" ")
print("\n")

for i in range(n-100): #O(n)
    print(i, end=" ")
print("\n")

for i in range(n*100): #O(n)
    print(i, end=" ")
print("\n")

for i in range(n//100): #O(n)
    print(i, end=" ")
print("\n")

for i in range(n): #O(n)
    for j in range(10):
        print(i, j, end=" ")
    print("\n")

#O(n+k)
for i in range(n):
    print(i, end=" ")

for i in range(k):
    print(i, end=" ")

#O(n^2)
for i in range(n):
    for j in range(n):
        print(i, j, end=" ")
        