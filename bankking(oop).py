class Bank:
    def __init__(self , balance):
        self.balance = balance
    def nap(self):
        amount=int(input("nhap so tien can nap"))
        self.balance+=amount

    def rut(self):
        amount=int(input("nhap so tien can rut"))
        if amount > self.balance:
            print("So du khong du ")
        else:
            self.balance-=amount

    def chuyen(self):
        while True:
            self.check = 0
            banks = {
                'Sacombank': {'name':'Sacombank', 'size_num': 12},
                'Vietcombank': {'name':'Vietcombank', 'size_num': 13},
                'Agribank': {'name':'Agribank', 'size_num': 13},
                'BIDV': {'name':'BIDV', 'size_num': 14},
                'MB Bank': {'name':'MB Bank', 'size_num': 16},
                'Acb': {'name':'Acb', 'size_num': 11},
                'Techcombank': {'name':'Techcombank', 'size_num': 14},
            }
            print("1.Sacombank")
            print("2.Vietcombank")
            print("3.Agribank")
            print("4.BIDV")
            print("5.MB Bank")
            print("6.Acb")
            print("7.Techcombank")
            oder =int(input("Lua chon ngan hang "))
            if(oder==1):
                bank_name = "Sacombank"
            elif(oder==2):
                bank_name = "Vietcombank"
            elif(oder==3):
                bank_name = "Agribank"
            elif(oder==4):
                bank_name = "BIDV"
            elif(oder==5):
                bank_name = "MB Bank"
            elif(oder==6):
                bank_name = "Acb"
            elif(oder==2):
                bank_name = "Techcombank"
            size_number = input("nhap so tai khoan ngan hang: ")
            if len(size_number) == banks[bank_name]["size_num"]:
                amount = int(input("nhap so tien can chuyen: "))
                if amount > self.balance:
                    print("So du khong du")
                else:
                    print("Chuyen tien thanh cong")
                    self.balance-=amount
                    self.check = 1
                    break
            else:
                print("Ngan hang hoac so tai khoan khong hop le")
                again = int(input("Moi quy khach nhap lai:"))
                oder = again

money=Bank(1000)
print("===Menu===")
print("chon 1 de kiem tra so du tai khoan")
print("chon 2 de nap tien vao tai khoan")
print("chon 3 de rut tien")
print("chon 4 de chuyen tien")
print("chon 5 de thoat giao dich")
print("=====&&&=====")
n =int(input())
while True:
    if n == 1:
        print(f"so du tai khoan: {money.balance}")
    elif n == 2:
        money.nap()
        print(f"so du tai khoan sau khi nap: {money.balance}")  
    elif n == 3:
        money.rut()
        print(f"so du tai khoan sau khi rut: {money.balance}")
    elif n == 5:
        print("cam on ban da su dung dich vu")
        break
    elif n == 4:
        money.chuyen()
    if money.check == 1:
        print(f"So du tai khoan: {money.balance}")
        print("===  ban co muon su dung dich vu khac khong?  ===")
        print("1.co")
        print("2.khong")
        choose = int(input())
        if(choose == 1):
            print("===  Menu  ===")
            print("chon 1 de kiem tra so du tai khoan")
            print("chon 2 de nap tien vao tai khoan")
            print("chon 3 de rut tien")
            print("chon 4 de chuyen tien")
            print("chon 5 de thoat giao dich")
            print("=====  &&&  =====")
            p = int(input())
            n = p
        else:
            print("cam on ban da su dung dich vu")
            break
