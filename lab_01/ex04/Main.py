from QuanLySinhVien import QuanLySinhVien

qlsv = QuanLySinhVien()
while (1 == 1):
    print("\nQuan Ly Sinh Vien")
    print("*************MENU***************************")
    print("**  1. Them SV                            **")
    print("**  2. Cao nhat thong tin sinh vien       **")
    print("**  3. Xoa SV theo Id                     **")
    print("**  4. Tim kiem SV theo ten               **")
    print("**  5. Sap xep SV theo diem               **")
    print("**  6. Sap xep SV theo chuyen nganh       **")
    print("**  7. Hien thi danh sach SV**")
    print("********************************************")

    key = int(input("Nhap tuy chon: "))

    if (key == 1):
        qlsv.NhapSinhVien()
    elif (key == 2):
        if(qlsv.SoLuongSinhVien() > 0):
            id = int(input("Nhap id SV can cap nhat: "))
            qlsv.UpdateSinhVien(id)
    elif (key == 3):
        if (qlsv.SoLuongSinhVien() > 0):
            id = int(input("Nhap id SV can xoa: "))

            if (qlsv.DeleteById(id)):
                print("\nSinh vien co id=", id, "da bi xoa.")
            else:
                print("\nSinh vien co id=", id," khong ton tai.")
        else:
            print("\nSanh sach sinh vien trong!")

    elif (key == 4):
        if (qlsv.SoLuongSinhVien() > 0):
            name = input("Nhap ten de tim kiem:")
            searchResult = qlsv.FindByName(name)
            qlsv.ShowSinhVien(searchResult)
        else:
            print("\nSanh sach sinh vien trong!")

    elif (key == 5):
        if (qlsv.SoLuongSinhVien() > 0):
            qlsv.SortByScore()
            qlsv.ShowSinhVien(qlsv.GetListSV())
        else:
            print("\nSanh sach sinh vien trong!")

    elif (key == 6):
        if (qlsv.SoLuongSinhVien() > 0):
            qlsv.SortByName()
            qlsv.ShowSinhVien(qlsv.GetListSV())
        else:
            print("\nSanh sach sinh vien trong!")

    elif (key == 7):
        if (qlsv.SoLuongSinhVien() > 0):
            qlsv.ShowSinhVien(qlsv.GetListSV())
        else:
            print("\nSanh sach sinh vien trong!")
    elif (key == 0):
        print("\nThoat chuong trinh")
    else:
        print("\nKhong hop le!")