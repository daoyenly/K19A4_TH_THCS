while True:
    n = int(input("Nhap n > 100: "))
    if n > 100:
        break
    print("Nhap lai!")

tong = 0
while n > 0:
    tong += n % 10
    n //= 10

print("Tong chu so:", tong)