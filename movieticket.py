#Movie ticket booking application
import time
from pytz import timezone
from datetime import datetime
userdatabase={'Yoga@gmail':['Yoga',123],'Priya@gmail':['Priya','56**'],'Mohitha@gmail':['Mohitha',789],'Ajitha@gmail':['Ajitha',101],'Birundha@gmail':['Birundha',201]}
class loginexistuser:
    def login(self):
        self.userid=input("Userid: ")
        self.password=input("Password: ")
    def welcome(self):
        c=userdatabase[user.userid]
        if((user.password)==str(c[1])):
                print("Welcome user !\n",c[0])
                time.sleep(3)
        else:
            print("Enter correct user details")
class signup:
    def sign(self):
        l=[]
        self.name=input("Name:")
        self.userid=input("Userid: ")
        self.password=input("Password: ")
        l.append(usersignup.name)
        l.append(usersignup.password)
        userdatabase[usersignup.userid]=l
class tamilmovie:
    def printmovie(self):
        print("--------List of movies in tamil--------\n")
        tamil=['Ps2','Varisu','KK','Thunivu']
        for i in tamil:
            print(i)
        time.sleep(3)
        
class telugumovie:
    def printmovie(self):
        print("-------List of movies in telugu--------\n")
        telugu=['Comrade','Gang','Majili','Vtv2']
        for j in telugu:
            print(j)
        time.sleep(3)
class hindimovie:
    def printmovie(self):  #polymorphism
        print("-------List of movies in hindi--------\n")
        hindi=['farzi','pathan']
        for k in hindi:
            print(k)
        time.sleep(3)
class book:
    def seatbook(self):
        self.history=[]
        a=[[1,2,3,4,5],
           [6,7,8,9,10],
           [11,12,13,14,15],
           [16,17,"Booked",19,20]]
        ticketcost=0
        n=int(input("Number of tickets"))
        while(n):
            movie=input("Booky my ticket for show: ")
            s=""
            ticketcount=0
            print("available seats: \n")
            for k in a:
                print(k,'\n')
            seat=int(input())
            for i in range(len(a)):
                for j in range(len(a[i])):
                    if(a[i][j]==seat):
                        ticketcount=1
                        a[i][j]="Booked"
                        time=datetime.now(timezone("Asia/Kolkata"))
                        s+="Movie: "
                        s+=movie 
                        s+=" , "
                        s+="Time:"
                        s+=str(time )
                        s+=" , "
                        s+="seat:"
                        s+=str(seat)
                        self.history.append(s)
                        if(i>2):
                           ticketcost=ticketcost+700 
                        else:
                            ticketcost=ticketcost+300
            if(ticketcount==1):
                print("Your seat has been booked")
                print(ticketcost)
                n=n-1
            else:
                print("Seat unavailable")
    def his(self):
        for itm in range(len(self.history)):
            print(self.history.pop())
    
user=loginexistuser()
usersignup=signup()
s=input()
if(s=="Login"):
    print("Enter your login details")
    user.login()
    user.welcome()
    
else:
    usersignup.sign()
    user.login()
    user.welcome()
tamil=tamilmovie()
telugu=telugumovie()
hindi=hindimovie()
tamil.printmovie()
telugu.printmovie()
hindi.printmovie()
