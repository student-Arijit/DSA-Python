#Best case = Ω(1)
#Avg. case = θ(n/2)
#worst case = O(n)

n = int(input("n = "))
x = int(input("x = "))

for i in range(n):
    if i == x:
        break

    print(i, end=" ")