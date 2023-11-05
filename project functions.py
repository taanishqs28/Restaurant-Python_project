from database import db,MyCur

def MDISPLAY():
    print('Our Menu is as Follows: ')
    SQL= "SELECT * FROM FOODITEMS"
    MyCur.execute(SQL)
    L=MyCur.fetchall()
    for sno, foodname, price,cuisine in L:
        print("%4d| %25s | %5d | %15s" %(sno,foodname.ljust(25,'_'),price,cuisine.ljust(15,' ')))
        

def CDISPLAY():
    print('Our Customer Table is :')
    SQL="SELECT * FROM CUSTOMERS"
    MyCur.execute(SQL)
    L=MyCur.fetchall()
    for CNAME,ADDRESS,MBNO,DIST in L:
        print("%25s | %35s | %10d | %20s" %(CNAME.ljust(25,' '),ADDRESS.ljust(35,' '),MBNO,DIST.ljust(20,' ')))


     

def AdminLogin():
    Username=input('Enter Username')
    Password=input('Enter Password')
    if Username in['ADMIN','admin','Admin'] and Password in ['1234']:

        print('Welcome Admin....')

        def Add():

            #ADD CUSTOMER
            def AddCustomer():
                try:
                
                    while True:
                        CName   =input('Enter Name of Customer       :')
                        Address =input('Enter the Address of Customer:')           
                        Mbno    =input('Enter Mbno of the Customer   :')
                        Dist    =input('Enter the District           :')
                        SQL="INSERT INTO CUSTOMERS VALUES('"\
                             +CName.upper()+"','"+Address+"',"+Mbno+",'"+Dist.upper()+"')"
                        MyCur.execute(SQL)
                        db.commit()
                        ch=input('Would Ypu Like to Add More?[Y/N]')
                        if ch in ['N','n']:
                            break
                    CDISPLAY()
                        
                except:
                    print('Looks Like something is wrong!')
                    print('try again!')
                


            
            #ADD FOOD
            def AddFood():
                try:                    
                    while True:
                        SNO     =input('SNO    :')
                        FOODNAME=input('Name   :')
                        PRICE   =input('Price  :')
                        CUISINE =input('Cuisine:')

                        SQL="INSERT INTO FOODITEMS VALUES("\
                         +SNO+",'"+FOODNAME.upper()+"'," +PRICE+",'"+CUISINE.upper()+"')"

                        MyCur.execute(SQL)

                        db.commit()
                        ch=input('Would Ypu Like to Add More?[Y/N]')
                        if ch=='N' or ch=='n':
                            break
                    
                    MDISPLAY()
                          
                except:
                    print('LOOKS LIKE SOMETHING IS WRONG,PLEASE TRY AGAIN!(TRY ENTERING A UNIQUE SNO)')
                    print()
            while True:
                print('What would you like to add?')
                ch=input('C: CUSTOMER  F: FOOD  E:Exit')
                if ch in['C','c']:
                    AddCustomer()
                elif ch in ['F','f']:
                    AddFood()
                elif ch in ['E','e']:
                    break                
                else:
                    print('You Entered the Wrong option')

        



        def EDIT():

            #Edit CUSTOMER
            def ECUS():
                Mb=input('Enter registered MbNO: ')
                sql="SELECT * FROM CUSTOMERS WHERE MBNO="+Mb+""
                N=MyCur.execute(sql)
                if N>0:
                    def Name():
                        Name=input('Enter New Name: ')
                        SQL="UPDATE CUSTOMERS SET CNAME='"+Name+"'"
                        MyCur.execute(SQL)
                        db.commit()
                        print('Table after addition:')
                        CDISPLAY()
                    def Address():
                        A=input('Enter New Address :')
                        SQL="UPDATE CUSTOMERS SET ADDRESS='"+A+"'"
                        MyCur.execute(SQL)
                        db.commit()
                        print('Table after addition:')
                        CDISPLAY()
                    while True:
                        print('What would you like to Edit?')
                        ch=input('A:Address , N:Name, E:Exit ')
                        if ch in ['A','a']:
                            Address()
                        elif ch in ['N','n']:
                            Name()
                        else:
                            break
                else:
                    print('Entered Number Does not exist!!')
                                           
                    
            def EFOOD():
                SNO= input('SNO:')
                SQL="SELECT * FROM FOODITEMS WHERE SNO="+SNO+""
                N= MyCur.execute(SQL)
                if N>0:
                    def FNAME():
                        Name=input('Enter new name for dish: ')
                        SQL="UPDATE FOODITEMS SET FOODNAME="+NAME+" WHERE SNO="+SNO+""
                        MyCur.execute(SQL)
                        db.commit()
                        print('Edited Table looks like: ')
                        CDISPLAY()
                

                    def EPrice():
                   
                        Price=input('Enter New Price')
                        SQL="UPDATE FOODITEMS SET PRICE="+Price+" WHERE SNO="+SNO+""
                        MyCur.execute(SQL)
                        db.commit()
                        print('Edited Table looks like: ')
                        MDISPLAY()
                        
                else:
                    print('You entered the wrong Sno')

            while True:
                ch=input('C:Edit_CUSTOMERS  F:EDIT_FOOD  E:Exit')
                
                if ch in ['C','c']:
                    ECUS()
                    
                elif ch in ['F','f']:
                    EFOOD()
                    
                else:
                    break

        def Delete():
           def DeleteCus():
               M=input("Enter Mbno of Customer : ")
               SQL="DELETE FROM CUSTOMERS WHERE MBNO="+M+""
               MyCur.execute(SQL)
               db.commit()
               print('The New Table is:')
               CDISPLAY()
               
           
           def DeleteFood():
                SNO= input("ENTER SNO OF ITEM YOU WANT TO DELETE: ")
                SQL="DELETE FROM FOODITEMS WHERE SNO="+SNO+""
                MyCur.execute(SQL)
                db.commit()
                print('The New Table is:')
                MDISPLAY()



           while True:
                ch=input('C:Delete_CUSTOMERS  F:Delete_FOOD E:Exit')
                if ch in ['C','c']:
                    DeleteCus()
                elif ch in ['F','f']:
                    DeleteFood()
                else:
                    break

               
        while True:
            x= input('A: ADD  E:EDIT D: DELETE  Q:QUIT: ')
            if x in ['A','a']:
                Add()
            elif x in ['E','e']:
                EDIT()
            elif x in ['D','d']:
                Delete()
            else:
                break
    else:
        print('You have entered the wrong Username or Password!!!')
            
        








#SALES LOGIN:
def SalesLogin():


    #1 Search:
    def Search():
        def Searchcustomer():
            try:
                MBNO=input("enter mobile number:")
                SQL="SELECT * FROM CUSTOMERS WHERE MBNO="+MBNO+""
                L=MyCur.execute(SQL)
                if L>0:
                    R=MyCur.fetchone()
                    print("found the customer details ")
                    print("CNAME             :",R[0])
                    print("ADDRESS           :",R[1])
                    print("MBNO              :",R[2])
                else:
                    print()
                    print("NO SUCH REGISTERED MOBILE NUMBER,KINDLY RE-ENTER MOBILE NUMBER")
            except:
                print()
                print("looks like something went wrong")

        def SearchFood():
            try:
                foodname=input("foodname :")
                SQL="SELECT * FROM FOODITEMS WHERE FOODNAME='"+foodname.upper()+"'"
                L=MyCur.execute(SQL)
                if L>0:
                    R=MyCur.fetchone()
                    print("found the item..")
                    print("sno.      :",R[0])
                    print("foodname  :",R[1])
                    print("price     : Rs.",R[2])
                else :
                    print()
                    print("Food Item doesn't exist")

            except:
                print()
                print("Something went wrong")

        while True:
            print('What do you want to Search?')
            ch=input('F: FoodItem  C: Customer  E:Exit')
            if ch in ['F','f']:
                SearchFood()
            elif ch in ['C','c']:
                Searchcustomer()
            else:
                break
                
    #2 Sort
    def Sort():
        #SORT BY NAME
        def SortCName():
            SQL="SELECT * FROM CUSTOMERS ORDER BY CNAME"
            MyCur.execute(SQL)
            R=MyCur.fetchall()
            for CNAME,ADDRESS,MBNO,DIST in R:
                print("%25s | %35s | %10d | %20s" %(CNAME.ljust(25,' '),ADDRESS.ljust(35,' '),MBNO,DIST.ljust(20,' ')))
        

        #Sorting FoodName(PRICE)
        def SortFood():
            SQL="SELECT * FROM FOODITEMS ORDER BY PRICE"
            N=MyCur.execute(SQL)
            R=MyCur.fetchall()
            for sno, foodname, price,cuisine in R:
                print("%4d| %25s | %5d | %15s" %(sno,foodname.ljust(25,'_'),price,cuisine.ljust(15,' ')))

        while True:
            print('What do you want to Sort?')
            ch=input('F: FoodItem  C: Customer  E:Exit')
            if ch in ['F','f']:
                SortFood()
            elif ch in ['C','c']:
                SortCName()
            else:
                break
                


    #3
    def Report():
        try:
            while True:
                Q={1:'How many Indian dishes do you serve?'\
                   ,2:'How many customers live in South Delhi?'\
                   ,3:'How many items are priced above Rs.175?'\
                   ,4:'What items are priced below Rs.150?',\
                   5:'Which is the most expensive dish?',\
                   6:'EXIT'}
                print(Q)
                x=int(input('Enter the Report number: '))
                if x==1:
                    SQL="SELECT COUNT(CUISINE) FROM FOODITEMS WHERE CUISINE='INDIAN'"
                    MyCur.execute(SQL)
                    n=MyCur.fetchone()
                    for i in n:
                        print('Number of Indian Dishes are: ',i)
                    print()
                elif x==2:
                    SQL="SELECT COUNT(DISTRICT) FROM CUSTOMERs WHERE DISTRICT='SOUTH DELHI'"
                    MyCur.execute(SQL)
                    n=MyCur.fetchone()
                    for i in n:
                        print('Number of Customers from South Delhi are: ',i)
                    print()
                    
                elif x==3:
                    SQL="SELECT COUNT(FOODNAME)FROM FOODITEMS WHERE PRICE>175"
                    MyCur.execute(SQL)
                    n=MyCur.fetchone()
                    for i in n:
                        print('Number of Dishes are: ',i)
                    print()
                elif x==4:
                    SQL="SELECT * FROM FOODITEMS WHERE PRICE<150"
                    MyCur.execute(SQL)
                    R=MyCur.fetchall()
                    
                    for sno, foodname, price,cuisine in R:
                        print("%4d| %25s | %5d | %15s" %(sno,foodname.ljust(25,'_'),price,cuisine.ljust(15,' ')))
                    print()
                elif x==5:
                    SQL="SELECT MAX(PRICE),FOODNAME,CUISINE FROM FOODITEMS GROUP BY CUISINE "
                    n=MyCur.execute(SQL)
                    R=MyCur.fetchall()
                    print(' PRICE  FOODNAME ')
                    for price,foodname,cuisine in R:
                        print("%5d | %25s | %15s" %(price,foodname.ljust(25,' '),cuisine.ljust(15,' ')))
                    print()
                else:
                    break
                    
        except:
            print('OOPS,YOU ENTERED THE WRONG REPORT NUMBER')
            print()
            print('PLEASE TRY AGAIN!!')
            print()
                        
    
    #4
    def Bill():        
        try:
            MDISPLAY()
            cost=0
            Y=[]
            while True:
                SNO=input('What would you like to order today(Enter No.)? ')
                qty=int(input('Enter Quantity: '))
                SQL="SELECT FOODNAME,PRICE FROM FOODITEMS WHERE SNO="+SNO+""
                MyCur.execute(SQL)
                X=MyCur.fetchone()
                Y.append(X)
                x=int(X[1])*qty
                cost+=x
                ch= input('More?(Y/N): ')
                if ch in ['N','n']:
                    break
            
            print('Your Order is:')
            print()         
            for foodname, price in Y:
                print("%25s | %5d" %(foodname.ljust(25,'_'),price))
            print()
            print('The Total Cost is: Rs.',cost)
                
        except:
            print('Something Went Wrong!')
            print('Please Try Again!!')
            
    #5
    def Query():
        try:
            while True:
                Q={1:'What are the timings?', 2: 'How much time does it take to complete the order?', 3:'Is Dine-in available?',\
                   4:'What Cuisines are available?',5:'Payment Methods used?'}
                print(Q)
                Ans={1:'Timings are 6 p.m.-11 p.m',2:'Around 35min to 40mins',\
                     3:'Yes, Dine-in is available, but unavailable due to COVID-19,only Take-Outs and Dilevery.'\
                     ,4:'Indian, Mughlai,Chinese',5:'Cash,Online Banking,PAYTM'}
                x=int(input('Enter the Query number: '))
                if x in [1,2,3,4,5]:
                    print('Query: ',Q[x])
                    print()
                    print('Answer: ',Ans[x])
                else:
                    break
        except:
            print('OOPS,YOU ENTERED THE WRONG QUERY NUMBER')
            print()
            print('PLEASE TRY AGAIN!!')
        
            
        
    






    
    while True:
        ch=input("M:MENU_DISPLAY  C:CUSTOMER_DISPLAY  S:SORT  O:SEARCH  B:BILL  Q:Query  R:REPORT  E:Exit: ")
        if ch in ['M','m']:
            MDISPLAY()
        elif ch in ['S','s']:
            Sort()
        elif ch in ['O','o']:
            Search()
        elif ch in ['B','b']:
            Bill()
        elif ch in ['Q','q']:
            Query()
        elif ch in ['C','c']:
            CDISPLAY()
        elif ch in ['R','r']:
            Report()
        elif ch in ['E','e']:
            break


print('WELCOME TO THE TRAVELLING INDIAN....')

print()

print('Who is logging in Today?')

print()

while True:
    ch=input('A: Admin Login  S: Sales Login  E: Exit: ')
    if ch in ['A','a']:
        AdminLogin()

    elif ch in ['S','s']:
        SalesLogin()

    elif ch in['E','e']:
        break
        
        
        
