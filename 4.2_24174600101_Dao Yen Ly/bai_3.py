while True:
    s = input("Nhap so: ")
    try:
        x = float(s)
        if x < 0 or not x.is_integer():
            print("Dung chuong trinh!")
            break
    except:
        print("Khong hop le!")