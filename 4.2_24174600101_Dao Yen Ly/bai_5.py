a = int(input("Nhap a: "))
b = int(input("Nhap b: "))

# Tính UCLN
x, y = a, b
while y != 0:
    x, y = y, x % y

ucln = x
print("UCLN:", ucln)

# BCNN
bcnn = abs(a*b) // ucln
print("BCNN:", bcnn)