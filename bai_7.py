while True:
    print("\nMenu:")
    print("1. Cafe")
    print("2. Cam vat")
    print("3. Nuoc ep ca rot")
    print("4. Nuoc loc")
    print("5. Nuoc dừa")
    print("0. Thoat")

    s = input("Chon: ")

    if not s.isdigit():
        print("Chon sai!")
        continue

    chon = int(s)

    if chon == 1:
        print("Ban chon Cafe")
    elif chon == 2:
        print("Ban chon Cam vat")
    elif chon == 3:
        print("Ban chon Nuoc ep ca rot")
    elif chon == 4:
        print("Ban chon Nuoc loc")
    elif chon == 5:
        print("Ban chon Nuoc dua")
    elif chon == 0:
        break
    else:
        print("Chon sai!")