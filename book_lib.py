import sys
from pymongo import MongoClient
import re
class Book:
    def __init__(self,amount=0):
        self.amount=amount
    def create(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["Book_of_India"]
        A_name=str(input("Enter the Author name:"))
        coll=dp["Books"]
        b_name=str(input("Enter the Book name:"))
        b_number=int(input("Enter how many Books:"))
        b_amount=int(input("Enter the Book Amount:"))
        coll.insert_one({"Book_Name":b_name,"Author_name":A_name,"Book_count":b_number,"amount":b_amount})
    def view(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["Book_of_India"]
        A_name=str(input("Enter the Author name:"))
        coll=dp["Books"]
        fin={"Author_name":A_name}
        for x in coll.find({},{"Book_Name":1,"Author_name":1,"Book_count":1,"amount":1}):
            print("Book_Name:",x["Book_Name"])
            print("Author_name:",x["Author_name"])
            print("Book_count:",x["Book_count"])
            print("amount:",x["amount"])
            print("\t=======================================================================================")
    def check_a(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["Book_of_India"]
        coll=dp["Books"]
        self.check_aa=input("Enter the Author Name:")
        for x in coll.find({"Author_name":self.check_aa}):
            return 1
    def check_b(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["Book_of_India"]
        coll=dp["Books"]
        self.check_bn=input("Enter the book Name:")
        for x in coll.find({"Book_Name":self.check_bn}):
            return 1
    def arrange(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["Book_of_India"]
        coll=dp["Books"]
        sor=coll.find({"Author_name":self.check_aa}).sort("Book_Name")
        if b.check_a()==1:
            for x in sor:
                print("Book_Name:",x["Book_Name"])
                print("Author_name:",x["Author_name"])
                print("Book_count:",x["Book_count"])
                print("amount:",x["amount"])
                print("\t=======================================================================================")
        else:
            print("\t\t!!!!Ther is no Data!!!!!")
    def darrange(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["Book_of_India"]
        coll=dp["Books"]
        if b.check_a()==1:
            sor=coll.find({"Author_name":self.check_aa}).sort("Book_Name",-1)
            for x in sor:
                print("Book_Name:",x["Book_Name"])
                print("Author_name:",x["Author_name"])
                print("Book_count:",x["Book_count"])
                print("amount:",x["amount"])
                print("\t=======================================================================================")
        else:
            print("\t\t!!!!Ther is no Data!!!!!")
    def buy_cd(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["Book_of_India"]
        coll=dp["Books"]
        self.sname=str(input("Enter the Customer Name:"))
        self.sno=input("Enter the Customer Mobile Number:")
        mn="[6-9][0-9]{9}"
        mv=re.match(mn,self.sno)
        if mv:
            if len(self.sno)==10:
                b.buy_b()
            else:
                print("Enter the Valid Number:")
        else:
            print("Enter the Valid Number format ")
    def buy_b(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["Book_of_India"]
        coll=dp["Books"]
        if b.check_a()==1:
            if b.check_b()==1:
                fn={"Book_Name":self.check_bn}
                fb=coll.find(fn)
                for x in fb:
                    no=x["Book_count"]
                    if no>0:
                        cou=int(input("how many books you want:"))
                        if cou>0:
                            mins=no-cou
                            print("\t\t==Remaining Book is ==",mins)
                            up={"$set":{"Book_count":mins}}
                            coll.update_one(fn,up)
                            af={"Book_Name":self.check_bn}
                            ab=coll.find(af)
                            for z in ab:
                                t=z["amount"]
                                total=t*cou
                                print(f" \t\t you purchesd {cou} books and the amount is {total}")
                                self.amount+=total
                                print(f" \t\t your bill total is over all purchesed {self.amount}" )
                                cn=client["Customer"]
                                cos_n=cn[self.sname]
                                cos_n.insert_one({"C_name":self.sname,"C_phone":self.sno,"B_name":self.check_bn,"B_rate":t,"N_book_brought":cou,"total":total,"O_all_rate":self.amount})
                        else:
                            print("!!!!Enter the correct value!!!!")
                            
                    else:
                        print("=== The Book is out of Stock!!!!===")
            else:
                print("\t\t!!!!Ther is no Data!!!!!")
        
        else:
            print("\t\t!!!!Ther is no Data!!!!!")
    def update_cou(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["Book_of_India"]
        coll=dp["Books"]
        if b.check_a()==1:
            if b.check_b()==1:
                bn={"Book_Name":self.check_bn}
                coun=int(input("Enter the count to be update:"))
                if coun>0:
                    bnu={"$set":{"Book_count":coun}}
                    coll.update_one(bn,bnu)
                else:
                    print("Enter the Valide input!!!")
            else:
                print("\t\t!!!!Ther is no Data!!!!!")
        else:
            print("\t\t!!!!Ther is no Data!!!!!")
    def update_rat(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["Book_of_India"]
        coll=dp["Books"]
        if b.check_a()==1:
            if b.check_b()==1:
                bn={"Book_Name":self.check_bn}
                coun=int(input("Enter the Rate to be update:"))
                if coun>0:
                    bnu={"$set":{"amount":coun}}
                    coll.update_one(bn,bnu)
                else:
                    print("Enter the Valide input!!!")
            else:
                print("\t\t!!!!Ther is no Data!!!!!")
        else:
            print("\t\t!!!!Ther is no Data!!!!!")
        
    def buyer_details(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["Customer"]
        A_name=str(input("Enter the Customer name to find:"))
        coll=dp[A_name]
        for x in coll.find({}):
            print("C_name:",x["C_name"])
            print("C_phone:",x["C_phone"])
            print("B_name:",x["B_name"])
            print("B_rate:",x["B_rate"])
            print("N_book_brought:",x["N_book_brought"])
            print("total:",x["total"])
            print("O_all_rate:",x["O_all_rate"])
            print("\t=======================================================================================")
    def  dele(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["Book_of_India"]
        coll=dp["Books"]
        if b.check_a()==1:
            if b.check_b()==1:
                md={"Book_Name":self.check_bn}
                coll.delete_one(md)
                print(f"\t\tYour Book {self.check_bn} is deleted succcesfully!!!! ")
            else:
                print("\t\t!!!!Ther is no Data!!!!!")
        else:
            print("\t\t!!!!Ther is no Data!!!!!")
    def user_op(self):
        print(f"\t  {1}-->To View the books \n\t {2}-->To see A-Z order the Book \n\t {3}-->To see Z-A order the book \n\t {4}--> To Buy the Book  \n\t {5}-->Quit")
        number1=int(input("enter the option:"))
        if number1==1:
            b.view()
        elif number1==2:
            b.arrange()
        elif number1==3:
            b.darrange()
        elif number1==4:
             b.buy_cd()
        elif number1==5:
            b.option()
    def main(self):
        if b.pass_check()==1:
            if b.pass_check1()==1:
                print(f"\t {1}-->if you want to insert the Book \n\t {2}-->To View the books \n\t {3}-->To see A-Z order the Book \n\t {4}-->To see Z-A order the book \n\t {5}--> To Buy the Book \n\t {6}-->To Buyer Details \n\t {7}-->update_count \n\t {8}-->update_Rate \n\t {9}-->delete \n\t {10}-->Change Password \n\t {11}-->quit")
                number=int(input("enter the option:"))
                if number==1:
                    q=int(input("how many books you want to insert:"))
                    for i in range(0,q):
                        b.create()
                elif number==2:
                    b.view()
                elif number==3:
                    b.arrange()
                elif number==4:
                    b.darrange()
                elif number==5:
                    b.buy_cd()
                elif number==6:
                    b.buyer_details()
                elif number==7:
                    b.update_cou()
                elif number==8:
                    b.update_rat()
                elif number==9:
                    b.dele()
                elif number==10:
                    b.pass_update()
                elif number==11:
                    b.option()
                    #print("\t\t You are exit the application now!!!")
                    #sys.exit("------------------------")
            else:
                print("Enter Valide formate password!!!!!!" )
        else:
            print("Enter Valide formate Id!!!!!!" )
        
    def option(self):
        print(f"\t If you are a \n\t 1.User \n\t 2.Admin")
        use_in=int(input("\t\t Enter the option:"))
        if use_in==1:
            b.user_op() 
        elif use_in==2:
            b.main()
        else:
            print("Enter the Correct Option!!!")
    def insert_ad(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["password"]
        coll=dp["Admin"]
        coll.insert_one({"User_id":self.idd,"User_pass":self.ipas})
    def check_pass(self):
        self.idd=input("Enter the Admin ID:")
        pat="^[a-z0-9]+\@[a-z]+\.[a-z]+$"
        self.vu=re.match(pat,self.idd)
        mn="^[A-Za-z0-9]+\@[0-9]+$"
        self.ipas=input("Enter the Admin Password:")
        self.pv=re.match(mn,self.ipas)
        if self.vu:
            if self.pv:
                b.insert_ad()
            else:
                print("Enter Valide formate password!!!!!!" )
        else:
            print("Enter Valide formate Id!!!!!!" )
    def pass_check(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["password"]
        coll=dp["Admin"]
        self.useid=input("Enter the Admin ID:")
        for x in coll.find({"User_id":self.useid}):
            return 1
    def pass_check1(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["password"]
        coll=dp["Admin"]
        self.usep=input("Enter the Admin password:")
        for x in coll.find({"User_pass":self.usep}):
            return 1
    def pass_update(self):
        client=MongoClient("mongodb://localhost:27017/")
        dp=client["password"]
        coll=dp["Admin"]
        if b.pass_check()==1:
            nep=input("Enter the New Password:")
            pa={"User_id":self.useid}
            pu={"$set":{"User_pass":nep}}
            coll.update_one(pa,pu)
        else:
            print("Contact the Service Provider!!!!")
b=Book()
while(True):
    b.option()
    
    
        
        
        
        
