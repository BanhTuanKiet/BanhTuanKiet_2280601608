soGioLam = float(input("Nhap so gio lam: "))
luongGio = float(input("Nhap luong gio lam: "))
gioTieuChuan = 44
gioVuotChuan = max(0, soGioLam - gioTieuChuan)
thucLinh = gioTieuChuan * luongGio + gioVuotChuan * luongGio

print(f"So tien thuc linh: {thucLinh}")