#When Someone Opens the page
# CEO USER ID= ONLINE_CLASSES_ARE_WORST 
# CEO PASSWORD= wewantschool
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import random as random
import requests
dso=[ ]
prdt1sele=[ ]
prdt2sele=[ ]
prdt3sele=[ ]
prdt4sele=[ ]
dummy1,dummy2,dummy3,dummy4=[],[],[],[]
cartele1=pd.DataFrame()
cartele2=pd.DataFrame()
cartele3=pd.DataFrame()
cartele4=pd.DataFrame()
emptycrt=np.array([["Face Mask (free)",0],["Face Shield",0]])
# ASSUMING ALREADY THREE CUSTOMERS HAVE REGISTERED
df_customer_records=pd.read_excel("C:\\ip/Customer records.xlsx" , header=None,names=['DOB','Gender','username','password','Email','Phone number'], index_col=None)
coupon_codes=pd.read_excel("C:\\ip/Coupon codes.xlsx" , header=None,names=['Code'], index_col=None)
couponlist=list(coupon_codes["Code"])
addele="X"
delivery_details="N"
dlt="S"
i=0
j=0
op=0
decisionYS=0
ipr1='Y'
editC="B"
po4=0
suma=0
decisionWS=0
G,ie="M","Y"
P,ds,ro="Y","Y",'Y'
cusdes4,gotoshop="S",'Z'
sele,sele2,sele3,sele4='Y',"Y","Y","Y"
loop_userid="Y"
querry='i'
password_user_signup=0
mano='Y'
LOGINMENU,productloop='Y','Y'
while mano=="Y":
  print("Hello! PERRENiAL™ welcomes you.\nChose the type of service you want. ")
  while j==0 or i=='N' or loop_userid=="Y" :
    print(" 'D'-DELIVERY DETAILS \n 'A'-ADMIN \n 'C'- CUSTOMER \n 'AB'-ABOUT PERRENiAL™   ")
    type= input("Choose your belonging : ")
    if type=="A":
      userid=input("CEO USER ID :  ")
      if userid=='ONLINE_CLASSES_ARE_WORST':
          i="Y"
          while (i==0 or i=='Y' or j=='N'):
            ceopassword=input("CEO PASSWORD :  ")
            if (ceopassword =="wewantschool"):
              print("Woaa! Look who is here. 'All the staffs start working properly the ADMIN is here',")
              while (op==0 or decisionYS=='N' or decisionWS=='N' or decisionDS=="N"):
                print(' 1. MONTHLY SALES \n 2. YEARLY SALES \n 3. WEEKLY SALES \n 4. WORKING POPULATION \n 5. DAILY ACTIVITY AND CUSTOMER RESPONSE\n 6.GO TO HOMEPAGE' )
                view=input("What bothers you the most")
                if(view=="2"):
                  decisionYS='Y'
                  while (decisionYS==0 or decisionYS=='Y'):
                    print(" 1. Yearly sales \n 2. Seller DataBase \n 3. Per year sales in category")
                    choose_yearlysales=input("Choose what you wanna see in Yearly sales")
                    if choose_yearlysales==("1"):
                      xYearlysales=[1,2,3,4,5,6,7,8,9,10,11,12]
                      yYearlysales=[776,752,766,749,778,678,687,677,656,788,787,887]
                      plt.plot(xYearlysales,yYearlysales,label="TOTAL SALES",color='r',marker="o",markerfacecolor="b")
                      month_name=['january',"february","march","april","may","june","july","august","september","october","november","december"]
                      plt.xticks(xYearlysales,month_name)
                      plt.grid(True)
                      plt.ylabel("no of products in thousands")
                      plt.legend()
                      plt.show()
                    elif choose_yearlysales==("3"):
                      x1=[1,2,3,4,5,6,7,8,9,10,11,12]
                      ycate1=[676,752,866,649,778,678,687,977,656,888,787,987]
                      ycate2=[250,300,444,535,533,646,742,300,454,545,400,455]
                      ycate3=[344,344,560,170,300,350,400,282,400,600,477,525]
                      ycate4=[687,822,792,766,653,780,680,599,888,779,821,666]
                      plt.plot(x1,ycate1,label="electronics",color='r',marker="o",markerfacecolor="b")
                      plt.plot(x1,ycate2,label="accesories",color='c',marker="+",markerfacecolor="k")
                      plt.plot(x1,ycate3,label="essenials",color='k',marker=">",markerfacecolor="c")
                      plt.plot(x1,ycate4,label="pantry",color='b',marker="<",markerfacecolor="y")
                      month_name=['january',"february","march","april","may","june","july","august","september","october","november","december"]
                      plt.xticks(x1,month_name)
                      plt.grid(True)
                      plt.ylabel("no of products in thousands")
                      plt.legend()
                      plt.show()
                    elif choose_yearlysales==("2"):
                      dfseller=pd.read_excel("C:\\ip/SB.xlsx" , header=None, names=['Seller name','Quantities sold','Rating','Returns & Replacements','Contact no','Membership'])  
                      print(dfseller.head(31))
                      print("These are the details regarding the sellers. Take a look.")
                    Yearlysalesloop=input("Y-wish to see some more stuff over hYEAR? \n N- Go back to admin page")
                    decisionYS=Yearlysalesloop
                elif(view=='3'):
                  decisionWS='Y'
                  while (decisionWS=="Y"):
                    print(" 1. Total sales \n 2. Sales DataBase ")
                    choose_weeklysales=input("Type what you wanna choose")
                    if choose_weeklysales==("1"):
                      xws=[1,2,3,4,5,6,7]
                      yws=[293,533,443,430,324,523,533]
                      plt.bar(xws,yws,label= "Total Sales",color='y', edgecolor='r', width=0.5)
                      bd=['Monday','Tuesday','Wednesday','Thursday','friday','saturday','Sunday']
                      plt.xticks(xws,bd)
                      plt.xlabel('Total sales')
                      plt.ylabel('Amount in thousands')
                      plt.legend()
                      plt.show()
                    elif choose_weeklysales==("2"):
                      dfWS=pd.read_excel("C:\\ip/WDB.xlsx" , header=None, names=['Days','Quantities sold','Returns','Exchange'])
                      print(dfWS)
                    decisionWS=input(" Y-Go to weekly sales again  \n N-Go to admin page")
                elif(view=="5"):
                  decisionDS='Y'
                  while (decisionDS=='Y'):
                    print('1. MOBILES SOLD IN LIGHTNING SALE \n2. SALES IN EACH CATEGORY OF THE DAY\n3. CUSTOMER QUERRY')
                    choose_dailysales=input("Enter what do you wanna choose")
                    if choose_dailysales=="1":
                      xM=[1,2,3,4,5]
                      yM=[233,534,243,543,333]
                      plt.bar(xM,yM,label= "Sales for diff smart phones",color='c', edgecolor='r', width=0.5)
                      phonebrand=['Samsung','Apple','Oneplus','Rog','Htc.']
                      plt.xticks(xM,phonebrand) 
                      plt.xlabel('Phone Brands')
                      plt.ylabel('Sales in no.')
                      plt.legend()
                      plt.show()
                    elif choose_dailysales=='2':
                      xD=[1,2,3,4,5,6,7,8,9,10,11,12]
                      yD1=[64,52,66,49,78,67,67,77,66,88,77,97]
                      yD2=[20,30,44,35,53,66,42,30,44,55,40,45]
                      yD3=[34,44,60,10,30,35,40,22,40,60,47,55]
                      yD4=[67,22,92,76,65,80,68,59,88,77,82,66]
                      plt.plot(xD,yD1,label="electronics",color='r',marker="o",markerfacecolor="b")
                      plt.plot(xD,yD2,label="accesories",color='c',marker="+",markerfacecolor="k")
                      plt.plot(xD,yD3,label="essenials",color='k',marker=">",markerfacecolor="c")
                      plt.plot(xD,yD4,label="pantry",color='b',marker="<",markerfacecolor="y")
                      timeday=['2am',"4am","6am","8am","10am","12pm","2pm","4pm","6pm","8pm","10pm","12am"]
                      plt.xticks(xD,timeday)
                      plt.grid(True)
                      plt.ylabel("no of products ordered")
                      plt.xlabel("Time")
                      plt.legend()
                      plt.show()
                    elif choose_dailysales=="3":
                      ro="Y"
                      while ro =='Y':
                        if querry=='i':
                          print("You have no Querries")
                          ro='N'                        
                        else:
                          print(querry)
                          print('This querry was submitted by', namecus,'\nPerennial has received a rating of ', rating,' from ', namecus )
                          queres=input("Enter your response for the customer's Querry sir:")
                          url = "https://www.fast2sms.com/dev/bulk"
                          payload={"sender_id":"FSTSMS",'message': "Hello " +namecus +'\n'+queres,"language":"english","route":"p","numbers":mobsup}
                          headers = {
                          'authorization': "uAMUXsroT0bGxNpdt82FSmR79B4ijcyfwn56QkVEIaJY1ZHqKLnseHLSWYiEhbCGzrZABtw2q9UPf1k6",
                          'Content-Type': "application/x-www-form-urlencoded",
                          'Cache-Control': "no-cache",
                          } 
                          response = requests.request("POST", url, data=payload, headers=headers)
                          print(response.text)
                          ro="N"
                    decisionDS=input("Y-Continue on daily sale \nN-Go to Admin homepage")
                elif(view=="1"):
                    decisionMS='Y'
                    while (decisionMS=='Y'):
                        print(" 1. MONTHLY SALES \n 2. MONTHLY SALES IN EACH CATEGORY \n 3. MONTHLY TURNOVER \n 4. MONTHLY DOWNLOADS \n 5. MONTHLY DONATED TO CHARITY \n 6. NUMBER OF PRODUCTS SOLD IN EACH CATEGORY THIS MONTH")
                        choose_monthlysales=input("WHAT DO YOU WANT TO SEE FROM THE ABOVE SIR?")
                        if(choose_monthlysales=="1"):
                          x=[1,2,3,4]
                          y=[29,38,40,35]
                          plt.plot(x,y,label="Amount In Crores",color="r",markerfacecolor="k") 
                          bd=["WEEK-1","WEEK-2","WEEK-3","WEEK-4"]
                          plt.xticks(x,bd)
                          plt.xlabel('Total sales')
                          plt.ylabel('Amount in Crorers')
                          plt.legend()
                          plt.show() 
                        elif(choose_monthlysales=="2"):
                          x=[1,2,3,4]
                          y=[10,13,15,12]
                          y2=[8,10,8,10]
                          y3=[6,7,9,5]
                          y4=[7,8,6,8]
                          plt.plot(x,y,label="electronics",color='b',marker=">",markerfacecolor="b")
                          plt.plot(x,y2,label="accesories",color='k',marker="<",markerfacecolor="k")
                          plt.plot(x,y3,label="essenials",color='c',marker="+",markerfacecolor="c")
                          plt.plot(x,y4,label="pantry",color='r',marker="o",markerfacecolor="y")
                          bd=['WEEK-1','WEEK-2','WEEK-3','WEEK-4']
                          plt.xticks(x,bd)
                          plt.ylabel("Amount in Crores")
                          plt.legend()
                          plt.show()
                        elif(choose_monthlysales=="3"):
                          x=[1,2,3,4]
                          y=[10,12.5,11,14]
                          plt.plot(x,y,label="Amount In Crores",color="k",markerfacecolor="r") 
                          bd=["WEEK-1","WEEK-2","WEEK-3","WEEK-4"]
                          plt.xticks(x,bd)
                          plt.xlabel('Total sales')
                          plt.ylabel('Amount in Crorers')
                          plt.legend()
                          plt.show()
                        elif(choose_monthlysales=="4"):                          
                          x=[1,2,3,4]
                          y=[44,50,48,52]
                          plt.bar(x,y,label= "MONTHLY DOWNLOADS",color='y', edgecolor='r', width=0.5)
                          bd=['WEEK-1','WEEK-2','WEEK-3','WEEK-4']
                          plt.xticks(x,bd)
                          plt.xlabel('MONTHLY DOWNLOADS')
                          plt.ylabel('NUMBER IN THOUSANDS')
                          plt.legend()
                          plt.show()
                        elif(choose_monthlysales=="5"):
                          print(" HAPPINESS IS THE ONE WHICH SHOULD BE SHARED TO EVERYONE!!!!! WE GIVE 25% OF OUR PROFIT TO CHARITY          ")
                          x=[1,2,3,4]
                          y=[2.5,3.125,2.75,3.5]
                          plt.bar(x,y,label= "MONTHLY DOWNLOADS",color='y', edgecolor='r', width=0.5)
                          bd=['WEEK-1','WEEK-2','WEEK-3','WEEK-4']
                          plt.xticks(x,bd)
                          plt.xlabel('MONTHLY DONATED')
                          plt.ylabel('AMOUNT IN CRORERS')
                          plt.legend()
                          plt.show()
                        elif(choose_monthlysales=="6"):
                          x=[1,2,3,4]
                          y=[565,540,670,590]
                          y2=[453,574,522,548]
                          y3=[344,387,429,450]
                          y4=[512,523,565,546]
                          plt.plot(x,y,label="electronics",color='r',marker="o",markerfacecolor="b")
                          plt.plot(x,y2,label="accesories",color='c',marker="+",markerfacecolor="k")
                          plt.plot(x,y3,label="essenials",color='k',marker=">",markerfacecolor="c")
                          plt.plot(x,y4,label="pantry",color='b',marker="<",markerfacecolor="y")
                          bd=['WEEK-1','WEEK-2','WEEK-3','WEEK-4']
                          plt.xticks(x,bd)
                          plt.ylabel("no of products in thousands")
                          plt.legend()
                          plt.show()
                        decisionMS=input(" Y-Continue on Monthly sale \n N-Go to Admin homepage ")     
                elif(view=="4"):
                  dfwp=pd.read_excel("C:\\ip/Delivery Executive DataBase.xlsx" , header=None, names=['Delivery Executive name','Years of experience','Rating','Customer Review','Perennial review','Id no.','Phone number'])
                  print(dfwp)
                  print("That's all to show in working population. Returning to Admin homepage")
                elif (view=="6"):
                  mano="Y"
                  break
                   
                else:
                  print("Enter the above options only with proper spellings")
              
            else:
              print("You are wrong")
              final_loop_password=input(" DO YOU WANT TO TRY AGAIN ? \nY - YES , N - GO TO HOMEPAGE ")
              i=final_loop_password
            break  
      else:
        loop_userid=0
        while loop_userid==0:
          print("User iD is invalid. Please try again.")
          loop_userid="Y"
                      
    elif type=="C":
      while P=="Y":
        print("Many wishes. One destination. Perennial™ welcomes you! \nis perennial already femiliar to you?")
        signup_login_user=input("'L'-Login to Perennial™ \n'S'-Become a new member of Perennial by signing up: ")
        if (signup_login_user=="S"):
          name_user_signup=input("Enter your full name ")
          dob_user_signup=input("Enter your dob in DD-MM-YYYY format ")
          while G=='M':
            Gender_user_signup=input('M , F , N (not to specify) ')
            if Gender_user_signup in ['M',"F","N"]:
              G="X"
            elif Gender_user_signup not in ['M',"F","N"]:
              G="M"
              print("Choose any one option only")
          username='Y'
          passi='y'
          ind='Y'
          while username=='Y':
            username_user_signup=input("Enter your username")    
            if(df_customer_records['username'].str.contains(username_user_signup).any()):
              print("Your username already exists. Please try a new one")
              username="Y"
            else:         
              username="N"
              while passi=='y':
                password_user_trial=input("Enter a password of atleast 5 charecters ")
                if len(password_user_trial) >= 5:
                  password_user_signup=password_user_trial
                  passi='n'         
                else:
                  print("please retry")
                  passi='y'
          email_user_signup=input("Enter avalid email id ")
          mobile_user_signup=(input("Enter a valid Phone (non dnd)number "))
          otpgen=str( random.randint(1000,9999))
          #OTP
          url = "https://www.fast2sms.com/dev/bulk"
          lang=input("Enter the language u want to receive your OTP.\n T-Tamil , E-English: ")
          if lang=='E':
            payload={"sender_id":"FSTSMS",'message': "Hello " +name_user_signup+ 'Many wishes, one destination. Perennial welcomes you  ' +'Your otp is'+otpgen,"language":"english","route":"p","numbers":mobile_user_signup}
            headers = {
            'authorization': "uAMUXsroT0bGxNpdt82FSmR79B4ijcyfwn56QkVEIaJY1ZHqKLnseHLSWYiEhbCGzrZABtw2q9UPf1k6",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            }
            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)
          elif lang=='T':
            payload={"sender_id":"FSTSMS",'message': "வணக்கம். அன்பான வரவேற்பு. உங்கள் otp- " + '  ' +otpgen,"language":"unicode","route":"p","numbers":mobile_user_signup}
            headers = {
            'authorization': "uAMUXsroT0bGxNpdt82FSmR79B4ijcyfwn56QkVEIaJY1ZHqKLnseHLSWYiEhbCGzrZABtw2q9UPf1k6",
            'Content-Type': "application/x-www-form-urlencoded",
            'Cache-Control': "no-cache",
            }
            response = requests.request("POST", url, data=payload, headers=headers)
            print(response.text)      
          ind="Y"
          while ind=='Y':
            otp_verify=int(input('Enter the otp: '))
            if otp_verify==int(otpgen):
              data={'DOB':[dob_user_signup],'Gender':[Gender_user_signup],"username":[username_user_signup],"password":[password_user_signup],"Email" : [email_user_signup],'Phone number' :[mobile_user_signup]}
              df_new_customer_records=pd.DataFrame(data, index=[name_user_signup])
              m=df_customer_records.append(df_new_customer_records)
              m.to_excel("C:\\ip/Customer records.xlsx", sheet_name='Account details' , index=True)
              ind='N'
            else:
              print('try again')
              ind="Y"
          P="No"    
        elif signup_login_user=='L' :
          while LOGINMENU =='Y':
            useri="Y"
            while useri=="Y":
              username_check=input("Enter your username: ")
              if(df_customer_records['username'].str.contains(username_check).any()):
                passie="y"
                while passie=='y':
                  user_password_check=input("Enter your password: ")
                  if(df_customer_records['password'].str.contains(user_password_check).any()):             
                    passie="n"
                  else:
                    print("wrong password.Try again")
                    passie="y"
                  useri='N'
                LOGINMENU='N'
              else:
                print("Username does not exist. Please try again")
                useri='Y'
                LOGINMENU="Y"
          P="No"    
        elif signup_login_user not in ["L","S"]:
          print("Choose any one option")
          P="Y"
      while productloop =='Y'or cusdes4=="S" or addele=="S" or goodbyeuser=="Y":
        gotoshop='Z'
        print ("Welcome to Perennial™"+"\n"+"Goods reach you.")
        customer_selection=input(" 1.Shop by Category \n 2.Cart \n 3.Customer Support \n 4.Confirm to signout")
        if customer_selection=='1'or gotoshop=="S":
          customer_cate_sele=input(" Here are the four different categories\n'1'-Electronics\n'2'-Pantry\n'3'-Essentials\n'4'-accessories :  ")
          sele="Y"
          while sele=="Y":
            if customer_cate_sele=='1':
              prdt1list=pd.read_excel("C:\\ip/Products list.xlsx" , sheet_name='Electronics',header=None, names=['Product Name','Price'], usecols="A,B" )
              print(prdt1list)
              while ipr1=="Y":
                prdt1seleinput=int(input("Enter the S.no of the product you want to buy: "))
                if prdt1seleinput>=0 and prdt1seleinput <=101:
                  prdt1sele.append(str(prdt1seleinput))
                  accept1=input("Do you want to continue shopping?\n'Y'-Yes\n'N'-No: ")
                  if accept1 =="Y":
                    ipr1="Y"
                  elif accept1=="N":
                    ipr1="N"
                  else:
                    ipr1='Y'
                    sele="n"
                else:
                  print("Enter the proper S.no of product")
                  sele='Y'
              for i in range(0, len(prdt1sele)):
                prdt1sele[i] = int(prdt1sele[i])
                dummy1.append(int(prdt1sele[i]))
                cartele1=pd.DataFrame(prdt1list.iloc[dummy1,[0,1]])
              elementscart=cartele1.values
              emptycrt=np.concatenate((emptycrt,cartele1)  , axis =0)
              dfcart=pd.DataFrame(emptycrt, columns=['Name','Price'])
              print(dfcart)
              sele='n'
              po=input("'C'-Go to homepage and continue to cart \n'S'-Go to Homepage and Continue shopping: ")
              if po=="C":
                 productloop="N"
              elif po=="S":
                productloop="Y"
            if customer_cate_sele=='2':
              prdt2list=pd.read_excel("C:\\ip/Products list.xlsx" , sheet_name='Pantry',header=None, names=['Product Name','Price'], usecols="A,B" )
              print(prdt2list)
              ipr2='Y'
              while ipr2=="Y":
                prdt2seleinput=int(input("Enter the S.no of the product you want to buy: "))
                if prdt2seleinput>=0 and prdt2seleinput <=70:
                  prdt2sele.append(str(prdt2seleinput))
                  accept2=input("Do you want to continue shopping?\n'Y'-Yes\n'N'-No: ")
                  if accept2 =="Y":
                    ipr2="Y"
                  elif accept2=="N":
                    ipr2="N"
                  else:
                    ipr2='Y'
                    sele="n"
                else:
                  print("Enter the proper S.no of product")
                  sele='Y'
              for i2 in range(0, len(prdt2sele)):
                prdt2sele[i2] = int(prdt2sele[i2])
                dummy2.append(int(prdt2sele[i2]))
                cartele2=pd.DataFrame(prdt2list.iloc[dummy2,[0,1]])
              elementscart=cartele2.values
              emptycrt=np.concatenate((emptycrt,cartele2)  , axis =0)
              dfcart=pd.DataFrame(emptycrt, columns=['Name','Price'])
              print(dfcart)
              sele='n'
              po2=input("'C'-Go to homepage and continue to cart\n'S'-Go to Homepage and Continue shopping: ")
              if po2=="C":
                productloop="N"
              elif po2=="S":
                print("\n")
                productloop="Y"
            if customer_cate_sele=='3':
              prdt3list=pd.read_excel("C:\\ip/Products list.xlsx" , sheet_name='Essentials',header=None, names=['Product Name','Price'], usecols="A,B" )
              print(prdt3list)
              ipr3='Y'
              while ipr3=="Y":
                prdt3seleinput=int(input("Enter the S.no of the product you want to buy: "))
                if prdt3seleinput>=0 and prdt3seleinput <=57:
                  prdt3sele.append(str(prdt3seleinput))
                  accept3=input("Do you want to continue shopping?\n'Y'-Yes\n'N'-No: ")
                  if accept3 =="Y":
                    ipr3="Y"
                  elif accept3=="N":
                    ipr3="N"
                  else:
                    ipr3='Y'
                    sele="n"
                else:
                  print("Enter the proper S.no of product")
                  sele='Y'
              for i3 in range(0, len(prdt3sele)):
                prdt3sele[i3] = int(prdt3sele[i3])
                dummy3.append(int(prdt3sele[i3]))
                cartele3=pd.DataFrame(prdt3list.iloc[dummy3,[0,1]])
              elementscart=cartele3.values
              emptycrt=np.concatenate((emptycrt,cartele3)  , axis =0)
              dfcart=pd.DataFrame(emptycrt, columns=['Name','Price'])
              print(dfcart)
              sele='n'
              po3=input("'C'-Go to homepage and continue to cart\n'S'-Go to Homepage and Continue shopping: ")
              if po3=="C":
                productloop="N"
              elif po3=="S":
                print("\n")
                productloop="Y"
                
            if customer_cate_sele=='4':
              prdt4list=pd.read_excel("C:\\ip/Products list.xlsx" , sheet_name='Accessories',header=None, names=['Product Name','Price'], usecols="A,B" )
              print(prdt4list)
              ipr4='Y'
              while ipr4=="Y":
                prdt4seleinput=int(input("Enter the S.no of the product you want to buy: "))
                if prdt4seleinput>=0 and prdt4seleinput <=49:
                  prdt4sele.append(str(prdt4seleinput))
                  accept4=input("Do you want to continue shopping?\n'Y'-Yes\n'N'-No: ")
                  if accept4 =="Y":
                    ipr4="Y"
                  elif accept4=="N":
                    ipr4="N"
                  else:
                    ipr4='Y'
                    sele="n"
                else:
                  print("Enter the proper S.no of product")
                  sele='Y'
              for i4 in range(0, len(prdt4sele)):
                prdt4sele[i4] = int(prdt4sele[i4])
                dummy4.append(int(prdt4sele[i4]))
                cartele4=pd.DataFrame(prdt4list.iloc[dummy4,[0,1]])
              elementscart=cartele4.values
              emptycrt=np.concatenate((emptycrt,cartele4)  , axis =0)
              dfcart=pd.DataFrame(emptycrt, columns=['Name','Price'])
              print(dfcart)
              sele='n'
              po4=input("'C'-Go to homepage and continue to cart\n'S'-Go to Homepage and Continue shopping: ")
              if po4=="C":
                productloop="N"
              elif po4=="S":
                print("\n")
                productloop="Y"
          sele="Y"
          po4="C"
        elif customer_selection=='2' or po4=="C" or po4=="S":
           print("Welcome to your cart")
           if po4==0:
             print("Your cart is empty")
             carsel=input("Do you want to shop ?\n'S'-Yes")
             if carsel=='S':
               gotoshop="S"
           elif po4=="C" or po4=="S" or delreturn=="S"  :
             delo="Y"
             while delo=="Y":
               print("Your Cart is -\n",dfcart)
               editcart=input("'E'-Edit the cart,\n'C'-Continue to checkout")
               if editcart=="E":
                 seledit=input('A-Add product to cart ( Continue shopping )\nD-Remove products\nC-Proceed to checkout')
                 if seledit=="A":
                   addele="S"
                   delo="N"
                 elif seledit=="D":
                   dlt="S"
                   while dlt=="S":
                     del_ele=int(input("Enter the serial no of product to be deleted"))
                     dfcart=dfcart.drop([del_ele])
                     print(dfcart)
                     ContDel=input("Do you want to delete some more items?\n Y-YES DELETE\n N-Proceed to cart")
                     if ContDel=="Y":
                       dlt="S"
                     elif ContDel=="N":
                       dlt="N"
                       delreturn="S"
                       delo="Y"
               elif editcart=="C":
                 print("Welcome to checkout\nThis is your cart :\n", dfcart ,"\n")
                 imo=0
                 suma=0
                 cart_total_price=list(dfcart["Price"])
                 while imo <len(cart_total_price):
                   suma= suma + int(cart_total_price[imo])
                   imo=imo+1
                 print("Total amount to be payed : ₹ ",suma)
                 delo="N"
                 coupask=input("Do you have any coupon code?\n Y-YES\n N-No")
                 if coupask=="Y":
                   coup="Y"
                   while coup=="Y":
                     coupinp=input("Enter the coupon code")
                     if coupinp in couponlist:
                       print ("Coupon valid\n")
                       coup="M"
                     else:
                       print("Coupon invalid\n")
                       v=input("Do you want to continue?\nY-YES\nN-NO")
                       if v=="Y":
                         coup="Y"
                       elif v=="N":
                         coup="N"
                 elif coupask=="N":
                   print("\nDelivery details(Enter Everything in CAPS: \n ")
                 deli_pincode=int(input("Enter your location's pincode :") )
                 deli_name=input("Enter your name: ")
                 deli_state=input("Enter your State(Free delivery inside TAMIL NADU): ")
                 if deli_state=="TAMIL NADU" or deli_state=="TAMIL NADU" :
                   print("No extra deliver charges")
                   del_charge=0
                 else:
                   print(" 100 rupees delivery charges")
                   del_charge=100
                 deli_city=input("Enter the city : ")
                 deli_address=input("Enter the Address : ")
                 deli_phone=int(input("Enter your phone number : "))
                 deli_payment=input("There are three modes of payment which will be done in the time of receiving the order(This is just a caution.Delivery agent will be having all three modes at the time of delivery):\n'CH'-Cheque(Should be handed over to the delivery agent on time of order delivery with proper account details(will be verified))\n'C'-Cash on delivery\n'CA'-Credit Cards(Credit cards will be swipped at the machine which is carried by the delivery agent) :")
                 if coupinp=="PER25OFF":
                   suma_discount=suma - ((25/100)*suma)
                 elif coupinp=="PER15OFF":
                   suma_discount=suma - ((15/100)*suma)
                 elif coupinp=="PER10OFF":
                   suma_discount=suma - ((10/100)*suma)
                 elif coupinp=="SIGNUPBONUS":
                   suma_discount=suma - ((13/100)*suma)
                 elif coupinp=="REBEL15":
                   suma_discount=suma - ((15/100)*suma)
                 elif coupinp=="WHATTY10":
                   suma_discount=suma - ((20/100)*suma)
                 elif coupinp=="BUY1GET1OFF":
                   suma_discount=suma - ((75/100)*suma)
                 else:
                   suma_discount=suma
                 print("Your Final cart:\n",dfcart,"\nYour bill :")
                 print("Total amount (Original amount) : ", suma,"\n\nAmount after discounts(Coupons applied if any) : ", suma_discount,"\n\nDelivery charges :",del_charge,"\n\nTotal payable amount :",(suma_discount + del_charge))
                 print("THANKYOU FOR SHOPPING WiTH US\nYour Order has been taken. You will get what you expected within 2-3 working days")
                 url = "https://www.fast2sms.com/dev/bulk"
                 payload={"sender_id":"FSTSMS",'message': 'Hello!'+deli_name+' Greetings fromm Perennial Team.Thankyou for shopping with us.\nThe product you orderdered will be soon delivered at'+deli_address+deli_city+deli_state+deli_pincode+'\nMode of payment : '+deli_payment+"Get 15 % OFF on your next Shopping use coupon code-'PER15OFF' ","language":"english","route":"p","numbers":deli_phone}
                 headers = {
                 'authorization': "uAMUXsroT0bGxNpdt82FSmR79B4ijcyfwn56QkVEIaJY1ZHqKLnseHLSWYiEhbCGzrZABtw2q9UPf1k6",
                 'Content-Type': "application/x-www-form-urlencoded",
                 'Cache-Control': "no-cache",
                 }
                 response = requests.request("POST", url, data=payload, headers=headers)
                 print(response.text)
                 print("\nREDIRECTING YOU TO HOMEPAGE")
                 delivery_details="S"
                 goodbyeuser="Y"

           mano='n'  
        elif customer_selection =='3':
          namecus=input("Enter your name")
          mobsup=int(input("Enter your valid (non DND) mobile number"))
          rat="Y"
          while rat=="Y":
            rating=int(input("Enter your rating for our service in a scale of 5"))
            if rating>=0 and rating<=5:
              rat="N"
            else:
              print("Enter your rating within a scale of 5")
              rat="Y"
          print("Welcome to Perennial Support centre. You are our Trea-sure!\nEmail-Perrenialcusup@gmail.com")
          url = "https://www.fast2sms.com/dev/bulk"
          payload={"sender_id":"FSTSMS",'message': 'Hello! Greetings fromm Perennial Team.Its always nice to have such great amazing customersas a member of the neverending family.Anytime, Perennial is yours. Contact about your reason for approaching Perennial at\n: Perennialcusup@gmail.com\nYours Truely and affordably\nPerrinial',"language":"english","route":"p","numbers":mobsup}
          headers = {
          'authorization': "uAMUXsroT0bGxNpdt82FSmR79B4ijcyfwn56QkVEIaJY1ZHqKLnseHLSWYiEhbCGzrZABtw2q9UPf1k6",
          'Content-Type': "application/x-www-form-urlencoded",
          'Cache-Control': "no-cache",
          }
          response = requests.request("POST", url, data=payload, headers=headers)
          print(response.text)
          print("We are sad to say to you that due to some reasons , we dont have a wide reaching phone number acces. I fyou have any querries, please do write it below.")
          querry=input('Enter your Querry')
          print("Please note. You will soon get a reply from the Bigg-boss. It usually takes 3 to 4 working days.\nThankyou for your patience")
          cusdes4=input("'C'-Proceed to cart\n'S'-Continue shopping: ")
          if cusdes4=='C':
            loop_userid="Y"
          elif cusdes4 =='S':
            productloop ='Y'
          productloop="Y"
          mano='n'
        elif customer_selection=='4':
          mano='Y'
          i=0
          j=0
          op=0
          decisionYS=0
          ipr1='Y'
          po4=0
          decisionWS=0
          G,ie="M","Y"
          P,ds,ro="Y","Y",'Y'
          cusdes4,gotoshop="S",'Z'
          sele,sele2,sele3,sele4='Y',"Y","Y","Y"
          loop_userid="Y"
          password_user_signup=0
          LOGINMENU ='Y'
          break
                 
          sele='Y'
    elif type=="AB":
      print("PERRENiAL™ is a conceptual online shopping prototype developed by ABHIEJIT KESHAVAN , AKASH NAWIN , PARASARAN for small scale purpose. This project involves the creation and signing in by the PERRENiAL™ customer account on the page which is especially designed for CUSTOMERS which is used as a tool for communication for customer feedback responses , delivery tracking details ,etc. Here the customer can look into various category of products available and then buy a product which they want.\n In the admin page , designed excusively for the admins, the boss can see the sales in  pictorially represented graphs.")
      mano="Y"
    elif type=="D":
      if delivery_details=="N":
        print("No recent items to be delivered")
      else:
        print("Order received:\n",'Customer Name : ',deli_name,'\nCustomer Phone number : ',deli_phone,'\n',dfcart,"\n","Total amount to be collected (including deliver charge) : " , (suma_discount + del_charge),'\nDelivery location : ',deli_address,' ',deli_city,' ',deli_state,' ',deli_pincode,"\nMode of payment : ", deli_payment)
               
    break          

    j=i
  mano='Y'
