# Nhap n > 0
while True:
    n = int(input("Nhap n > 0: "))
    if n > 0:
        break
    print("Nhap lại!")

# a. S1 = 1^2 + 2^2 + ... + n^2
S1 = 0
for i in range(1, n + 1):
    S1 += i**2
print("S1 =", S1)

# b. S2 = 1^3 + 3^3 + ... + (2n+1)^3
S2 = 0
i = 0
while i <= n:
    S2 += (2*i + 1)**3
    i += 1
print("S2 =", S2)

# c. S3 = 2^4 + 4^4 + ... + (2n)^4
S3 = 0
for i in range(1, n + 1):
    S3 += (2*i)**4
print("S3 =", S3)

# d. S4 = 1/1 - 1/2 + 1/3 - ... + (-1)^(n-1)/n
S4 = 0
i = 1
while i <= n:
    S4 += ((-1)**(i-1)) / i
    i += 1
print("S4 =", S4)

# e. S5 = 1/2 + 1/(2*3) + 1/(3*4) + ... + 1/(n(n+1))
S5 = 0
for i in range(1, n + 1):
    S5 += 1 / (i * (i + 1))
print("S5 =", S5)

# f. S6 = 1/sqrt(2) + 1/sqrt(3) + ... + 1/sqrt(n)
import math
S6 = 0
i = 2
while i <= n:
    S6 += 1 / math.sqrt(i)
    i += 1
print("S6 =", S6)