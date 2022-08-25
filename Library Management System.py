print("LIBRARY MANAGEMENT SYSTEM")
class Books(list):
    def Load_Book(self):
        f = open('Books.txt', 'a+')
        f.seek(0)
        for record in f: self.append(eval(record))
        f.close()
    def Add_Book(self):
        print("ADD THE NEW PRODUCT BELOW")
        self.title = input("BOOK TITLE       : ")
        self.author = input("BOOK AUTHOR      : ")
        self.subject = input("SUBJECT          : ")
        self.publication_date = input("PUBLICATION DATE : ")
        self.quantity = int(input("ADD QUANTITY     : "))
        self.append([self.title, self.author, self.subject, self.publication_date,self.quantity])
        f = open('Books.txt', 'a+')
        f.seek(0)
        for record in self: f.write(str(record) + '\n')
        f.close()
        print("BOOK SAVED ... :) ")
    def Remove_Book(self):
        self.Load_Book()
        Search = input("Enter Book Name: ")
        for Book in self:
            if Book[0] == Search:
                self.remove(Book)
                f = open('Books.txt', 'w+')
                for record in self:
                    f.write(str(record) + '\n')
                f.close()
                print("BOOK DELETED")
                break
        else:
            print("BOOK NOT FOUND")
    def Search_Catalogue(self):
        self.Load_Book()
        Search = input("Enter Book Title : ")
        for Book in self:
            if Book[0] == Search:
                print('BELOW IS BOOK INFORMATION:')
                print('\t BOOK TITLE          : ', Book[0])
                print('\t BOOK AUTHOR         : ', Book[1])
                print('\t SUBJECT             : ', Book[2])
                print('\t PUBLICATION DATE    : ', Book[3])
                break
        else:
            print('     BOOK NOT FOUND :( ')
    def Check_Out_Book(self,filename,ID):
        self.Load_Book()
        Book_Needed = input("ENTER BOOK NAME   : ")
        for Book in self:
            if Book[0] == Book_Needed:
                if Book[4] != 0:
                    self.append([Book[0],Book[1], Book[2], Book[3], int(Book[4]) - 1])
                    self.remove(Book)
                    file = open(filename, 'a+')
                    file.write(str(Book[0:3]) + '\n')
                    file.close()
                    file = open('Books.txt', 'w+')
                    for record in self:
                        file.write(str(record) + '\n')
                    file.close()
                    break
                else:
                    print("SORRY. BOOK IS OUT OF STOCK.")
                    Select = int(input("PRESS 1 TO RESERVE : "))
                    if Select == 1:
                        self.Reserve_Book(Book_Needed,ID)
                        break
        else: print("BOOK NOT AVAILABLE")
    def Reserve_Book(self,Book,ID):
        Reserve = [ID,Book]
        file = open('Reserved_Books.txt', 'a+')
        file.write(str(Reserve) + '\n')
        file.close()
        print("BOOK RESERVED... TILL THEN PLEASE WAIT.")
    def Book_List(self):
        self.Load_Book()
        print('DISPLAY: AVAILABLE BOOKS')
        Serial = 1
        for record in self:
            print(f'*|*  {Serial:003}. Name : {record[0]:20} - Author: {record[1]}')
            Serial += 1
class Member(list):
    def __init__(self):
        super().__init__()
        print('1. REGISTER NEW ACCOUNT')
        print('2. LOGIN')
        print('3. CANCEL MEMBERSHIP')
        Select = int(input("Select : "))
        if Select == 1:
            self.Register_New_Account()
        elif Select == 2:
            self.Sign_In()
        elif Select == 3:
            self.Cancel_Membership()
    def Register_New_Account(self):
        Name = input('Enter Username    : ')
        Pswd = input('Set Password      : ')
        file = open('ID_Number.txt', 'a+')
        ID = file.read()
        file = open('ID_Number.txt', 'w')
        file.write(str(ID))
        file.close()
        filename = 'User_ID_' + str(ID) + '.txt'
        file = open('User_Accounts.txt', 'a+')
        file.write(str([Name, Pswd, ID, filename]) + '\n')
        file.close()
        OBJ = Books()
        OBJ.Check_Out_Book(filename,ID)
    def Sign_In(self):
        self.Load_Accounts()
        Name = input('Enter Username : ')
        Pswd = input('Enter Password : ')
        for Account in self:
            if Name == Account[0] and Pswd == Account[1]:
                print("WELCOME!! Wanna?")
                print(" 1. CHECKOUT BOOK?\n 2. RENEW BOOK?\n 3. RETURN BOOK?")
                Select = int(input("SELECT: "))
                OBJ = Books()
                if Select == 1:
                    OBJ.Check_Out_Book(Account[3],Account[2])
                elif Select == 2:
                    OBJ.Renew_Book(Account[3])
                elif Select == 3:
                    OBJ.Return_Book(Account[3])
    def Cancel_Membership(self):
        self.Load_Accounts()
        Name = input('Enter Username : ')
        Pswd = input('Enter Password : ')
        for Account in self:
            if Name == Account[0] and Pswd == Account[1]:
                self.remove(Account)
                file = open('User_Accounts.txt', 'w+')
                for record in self:
                    file.write(str(record) + '\n')
                file.close()
                print("MEMBERSHIP CANCELLED")
    def Load_Accounts(self):
        file = open('User_Accounts.txt', 'a+')
        file.seek(0)
        for record in file:
            self.append(eval(record))
        file.close()
class Admin(Books):
    def __init__(self):
        super().__init__()
        Admin_ID = int(input("Enter ID Please (Number): "))
        Admin_Password = input("Enter Password Please   : ")
        if Admin_ID == 2 and Admin_Password == "SYSTEM FAIL":
            print('WELCOME TO ADMIN!! WANNA? !!!')
            print('1.  ADD BOOK\n2.  REMOVE BOOK\n3.  SEARCH BOOK\n4.  DISPLAY BOOKS\n6.  EXIT.')
            Select = int(input("SELECT: "))
            if Select == 1: self.Add_Book()
            elif Select == 2: self.Remove_Book()
            elif Select == 3: self.Search_Catalogue()
            elif Select == 5: self.Book_List()
        else:
            print('INCORRECT INFORMATION ABOUT ADMIN ADDED.')
# Object Code
print('*** Welcome to the Library *** \n1. Administrator\n2. User/Member\n3. Exit')
while True:
    
    Select = int(input('Select : '))
    if Select == 1: Admin()
    elif Select == 2: Member()
