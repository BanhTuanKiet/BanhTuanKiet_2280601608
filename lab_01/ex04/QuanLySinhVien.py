from SinhVien import SinhVien

class QuanLySinhVien:
    listSinhVien = []

    def GenerateID(self):
        maxId = 1

        if (self.SoLuongSinhVien() > 0):
            maxId = self.listSinhVien[0].id

            for sv in self.listSinhVien:
                if (maxId < sv.id):
                    maxId = sv.id
            
            maxId = maxId + 1
        
        return maxId

    def SoLuongSinhVien(self):
        return self.listSinhVien.__len__()
    
    def NhapSinhVien(self):
        id = self.GenerateID()
        name = input("Nhap ten: ")
        sex = input("Nhap gioi tinh: ")
        major = input("Nhap chuyen nganh: ")
        score = float(input("Nhap diem: "))

        sv = SinhVien(id, name, sex, major, score)
        self.XepLoaiHocLuc(sv)
        self.listSinhVien.append(sv)

    def DeleteById(self, id):
        sv:SinhVien = self.FindById(id)

        if (sv != None):
            self.listSinhVien.remove(sv)
            return True

        return False

    def UpdateSinhVien(self, id):
        sv:SinhVien = self.FindById(id)

        if (sv != None):
            name = input("Nhap ten: ")
            sex = input("Nhap gioi tinh: ")
            major = input("Nhap chuyen nganh: ")
            score = float(input("Nhap diem: "))

            sv.name = name
            sv.sex = sex
            sv.major = major
            sv.score = score
            self.XepLoaiHocLuc(sv)
        else:
            print("Sinh vien co Id = {} khong ton tai.".format(id))
    
    def SortById(self):
        self.listSinhVien.sort(key=lambda x: x.id, reverse=False)

    def SortByName(self):
        self.listSinhVien.sort(key=lambda x: x.name, reverse=False)

    def SortByScore(self):
        self.listSinhVien.sort(key=lambda x: x.score, reverse=False)

    def FindById(self, id):
        searchRes = None
        
        if (self.SoLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (sv.id == id):
                    searchRes = sv
                    break

        return searchRes
    
    def FindByName(self, keyword):
        listSV = []
        
        if (self.SoLuongSinhVien() > 0):
            for sv in self.listSinhVien:
                if (keyword.upper() in sv.name.upper()):
                    listSV.append(sv)
                    
        return listSV
    
    def XepLoaiHocLuc(self, sv:SinhVien):
        if (sv.score >= 8):
            sv.rank = "A"
        elif (sv.score >= 6.5):
            sv.rank = "B"
        elif (sv.score >= 5):
            sv.rank = "C"
        else:
            sv.rank = "D"

    def ShowSinhVien(self, listSV):
        print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
              .format("ID", "NAME", "SEX", "MAJOR", "SCORE", "RANK")
              )
        
        if (listSV.__len__() > 0):
            for sv in listSV:
                print("{:<8} {:<18} {:<8} {:<8} {:<8} {:<8}"
                      .format(sv.id, sv.name, sv.sex, sv.major, sv.score, sv.rank)
                      )
        
        print("\n")

    def GetListSV(self):
        return self.listSinhVien
