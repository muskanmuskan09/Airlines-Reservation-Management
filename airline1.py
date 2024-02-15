from tkinter import *
import datetime as dt
from PIL import ImageTk
from tkinter import ttk
from tkinter import messagebox
import cx_Oracle
#Functionality



def ticket_click():
   if IDEntry.get()=='' or  passEntry.get()=='' or flightEntry.get()=='' or seatEntry.get()=='' or mobEntry.get()=='' or addressEntry.get()=='' or statusEntry.get()=='':
      messagebox.showerror('Error',"All fields are required")
   else:
      conn = cx_Oracle.connect(user='C##892', password='892')
      cur = conn.cursor()
      a = f"insert into passenger values('{IDEntry.get() }','{passEntry.get()}','{flightEntry.get()}','{seatEntry.get()}','{mobEntry.get()}','{addressEntry.get()}','{statusEntry.get()}')"
      cur.execute(a)
      conn.commit()
      messagebox.showinfo('Success', 'Your Ticket has been Booked')
      cur.close()
      conn.close()


# To check Availability of Flights
def Avail_flight():
   conn=cx_Oracle.connect("airline/mmmk")
   cur=conn.cursor()
   print(conn.version)

   sql="select* from flights"
   cur.execute(sql)
   rows=cur.fetchall()
   win=Tk()
   frame=Frame(win)
   frame.pack(side=LEFT)


   tv=ttk.Treeview(frame,columns=(1,2,3,4,5,6,7,8,9),show="headings",height="30")
   tv.grid(row=1,column=1,columnspan=2,padx=10,pady=10)
   tv.column(1 ,anchor=CENTER,width=30)
   tv.heading(1,text="FlightNo")
   tv.column(2, anchor=CENTER, width=170)
   tv.heading(2,text="Flightname")
   tv.column(3, anchor=CENTER, width=170)
   tv.heading(3,text="Source")
   tv.column(1, anchor=CENTER, width=170)
   tv.heading(4,text="Destination")
   tv.column(5, anchor=CENTER, width=100)
   tv.heading(5, text="Departure Time")
   tv.column(6, anchor=CENTER, width=100)
   tv.heading(6, text="Arrival Time", anchor=CENTER)
   tv.column(7, anchor=CENTER, width=100)
   tv.heading(7, text="Fare")
   tv.column(8, anchor=CENTER, width=100)
   tv.heading(8, text="Filled seats")
   tv.column(9, anchor=CENTER, width=100)
   tv.heading(9, text="Empty seats")

   for i in rows:
     tv.insert('','end',values=i)

   style=ttk.Style(win)
   style.theme_use('clam')

   style.configure("Treeview",background="grey",foreground="black",font=("Times",12,'normal'),rowheight=30,fieldbackground="powderblue")
   style.configure("Treeview.Heading",background='cyan3')
   win.title("flight details")
   win.geometry("1279x600+50+100")
   win.mainloop()



#For Booking Ticket
def book_ticket():
   window=Toplevel()
   window.geometry("1279x600+50+100")
   window.resizable(False, False)
   window.title('Book ticket')
   global IDEntry
   global passEntry
   global flightEntry
   global seatEntry
   global mobEntry
   global addressEntry
   global  statusEntry
   bgImage = ImageTk.PhotoImage(file="down.jpg")
   bgLabel = Label(window, image=bgImage)
   bgLabel.place(x=0, y=0)
   label=Label(window,text="Passenger Id",font=('monotype 12 bold'),foreground='Black',background='white',width=15)
   label.place(x=200,y=30)
   IDEntry = Entry(window, width=27, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='black')
   IDEntry.place(x=400, y=30)

   label = Label(window, text="Passenger Name", font=('monotype 12 bold'),foreground='Black',background='white',width=15)
   label.place(x=200, y=80)
   passEntry = Entry(window, width=27, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='black')
   passEntry.place(x=400, y=80)

   label = Label(window, text="DOB", font=('monotype 12 bold'), foreground='Black', background='white',width=15)
   label.place(x=200, y=130)
   flightEntry = Entry(window, width=27, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='black')
   flightEntry.place(x=400, y=130)

   label = Label(window, text="Mobile no", font=('monotype 12 bold'), foreground='Black', background='white',width=15)
   label.place(x=200, y=180)
   seatEntry = Entry(window, width=27, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=1, fg='black')
   seatEntry.place(x=400, y=180)

   label = Label(window, text="Address",font=('monotype 12 bold'), foreground='Black', background='white',width=15)
   label.place(x=200, y=230)
   mobEntry = Entry(window, width=27, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='black')
   mobEntry.place(x=400, y=230)

   label = Label(window, text="Class", font=('monotype 12 bold'), foreground='Black', background='white',width=15)
   label.place(x=200, y=280)
   addressEntry = Entry(window, width=27, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='black')
   addressEntry.place(x=400, y=280)

   label = Label(window, text="Flight No", font=('monotype 12 bold'), foreground='Black', background='white',width=15)
   label.place(x=200, y=330)
   statusEntry = Entry(window, width=27, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='black')
   statusEntry.place(x=400, y=330)

   ticketButton = Button(window, text='Book Ticket', font=('Open Sans', 16, 'bold'), bd=0, fg='white', bg='blue',
                        activeforeground='white',
                        activebackground='blue', cursor='hand2', width=10,command=ticket_click)
   ticketButton.place(x=400, y=450)

   window.mainloop()

def get_ticket():
   window=Toplevel()
   window.geometry("1279x600+50+100")
   window.resizable(False, False)
   window.title('Get ticket')
   bgImage = ImageTk.PhotoImage(file="down.jpg")
   bgLabel = Label(window, image=bgImage)
   bgLabel.place(x=0, y=0)



   headingLabel = Label(window, text="Spark Airlines-Ticket Window", font=("Impact", 20), bg='white',fg='black',
                        width=29, bd=2, height=2)
   headingLabel.place(x=800, y=50)
   getticketButton = Button(window, text='Get Ticket', font=('Open Sans', 16, 'bold'), bd=0, fg='white', bg='blue',
                         activeforeground='white',
                         activebackground='blue', cursor='hand2', width=10)
   getticketButton.place(x=490,y=30)
   # for passenger id
   passIDLabel = Label(window, text="Enter your passenger ID", font=("Open sans", 15), fg='black', bg='white',
                       width=20, bd=2)
   passIDLabel.place(x=80, y=30)
   IDEntry = Entry(window, width=6, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   IDEntry.place(x=380, y=30)

   # Inside Frame

   frame2 = Frame(window, bg="blue", highlightthickness=4)
   frame2.place(x=50, y=100, height=440, width=580)

   # for passenger name
   passnameLabel = Label(window, text="Passenger Name", font=("Open sans", 15), fg='black', bg='white', width=20,
                         bd=2)
   passnameLabel.place(x=80, y=120)
   nameEntry = Entry(window, width=15, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   nameEntry.place(x=350, y=120)

   # for passenger flight no
   flightno_Label = Label(window, text="Flight No", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
   flightno_Label.place(x=80, y=170)
   flightnoEntry = Entry(window, width=15, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   flightnoEntry.place(x=350, y=170)

   # for passenger class

   classLabel = Label(window, text="Class", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
   classLabel.place(x=80, y=220)
   classEntry = Entry(window, width=15, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   classEntry.place(x=350, y=220)

   # for flight name

   flightnameLabel = Label(window, text="Flight Name", font=("Open sans", 15), fg='black', bg='white', width=20,
                           bd=2)
   flightnameLabel.place(x=80, y=270)
   flight_nameEntry = Entry(window, width=15, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   flight_nameEntry.place(x=350, y=270)

   # for source

   sourceLabel = Label(window, text="Source", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
   sourceLabel.place(x=80, y=320)
   sourceEntry = Entry(window, width=15, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   sourceEntry.place(x=350, y=320)

   # for destination

   destinationLabel = Label(window, text="Destination", font=("Open sans", 15), fg='black', bg='white', width=20,
                            bd=2)
   destinationLabel.place(x=80, y=370)
   destinationEntry = Entry(window, width=15, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   destinationEntry.place(x=350, y=370)

   # for departure time

   departureLabel = Label(window, text="Departure Time ", font=("Open sans", 15), fg='black', bg='white', width=20,
                          bd=2)
   departureLabel.place(x=80, y=420)
   dtimeEntry = Entry(window, width=15, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   dtimeEntry.place(x=350, y=420)

   # for arrivaltime

   arrivaLabel = Label(window, text="Arrival Time", font=("Open sans", 15), fg='black', bg='white', width=20, bd=2)
   arrivaLabel.place(x=80, y=470)
   atimeEntry = Entry(window, width=15, font=("Microsoft yahei yI Light", 15, "bold"), bd=2, fg='black')
   atimeEntry.place(x=350, y=470)



   window.mainloop()

def cancel_flight():
   window=Toplevel()
   window.geometry("1279x600+50+100")
   window.resizable(False, False)
   window.title('Cancel reservation')
   bgImage = ImageTk.PhotoImage(file="down.jpg")
   bgLabel = Label(window, image=bgImage)
   bgLabel.place(x=0, y=0)

   flightno_label= Label(window, text="Flight Number", font=('monotype 12 bold'), foreground='Black', background='white',width=15)
   flightno_label.place(x=100, y=130)
   flightnoEntry= Entry(window, width=27, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='black')
   flightnoEntry.place(x=300, y=130)
   seatno_label = Label(window, text="Seat Number", font=('monotype 12 bold'), foreground='Black',background='white',width=15)
   seatno_label.place(x=100, y=200)
   seatnoEntry = Entry(window, width=27, font=('Microsoft Yahei UI Light', 11, 'bold'), bd=0, fg='black')
   seatnoEntry.place(x=300, y=200)

   CancelButton = Button(window, text='Cancel Ticket', font=('Open Sans', 16, 'bold'), bd=0, fg='white', bg='blue',
                         activeforeground='white',
                         activebackground='blue', cursor='hand2', width=15)
   CancelButton.place(x=250, y=300)

   window.mainloop()




airline=Tk()
#airline.geometry("1279x1392+0+0")
airline.geometry("1279x600+50+100")
airline.resizable(False,False)
airline.title("Airlines")

bgImage=ImageTk.PhotoImage(file="aeroplane4.jpg")
bgLabel=Label(airline,image=bgImage)
bgLabel.place(x=0,y=0)

date=dt.datetime.now()
label=Label(airline,text=f"{date:%A,%B,%d,%Y}",font="Calibri,20,bold",fg="black")
label.place(x=1000,y=550)


heading=Label(airline,text='Welcome to Spark Airlines',font=("Impact",30,"bold underline"),fg='black',bg="turquoise2")
heading.place(x=400,y=10)

#Frame_login=Frame(airline,bg="white",highlightbackground='black',highlightthickness=5)
#Frame_login.place(x=120,y=90,height=400,width=350)

#back_login=Button(airline,text='Back to Login',font=("Open Sans",10,'bold' ),fg='white',bg='black',activebackground="black",activeforeground="white",command=Back_login)
#back_login.place(x=240,y=450)

Button_1=Button(airline,text='Available flights',font=('monotype 12 bold'),bg='white',fg='black',activebackground='white',activeforeground='black',command=Avail_flight)
Button_1.place(x=150,y=150,width=270,height=50)
Button_2=Button(airline,text='Book flight',font=('monotype 12 bold'),bg='white',fg='black',activebackground='white',activeforeground='black',command=book_ticket)
Button_2.place(x=150,y=220,width=270,height=50)
Button_3=Button(airline,text='Get Ticket',font=('monotype 12 bold'),bg='white',fg='black',activebackground='white',activeforeground='black',command=get_ticket)
Button_3.place(x=150,y=290,width=270,height=50)
Button_3=Button(airline,text='Cancel flights',font=('monotype 12 bold'),bg='white',fg='black',activebackground='white',activeforeground='black',command=cancel_flight)
Button_3.place(x=150,y=360,width=270,height=50)

airline.mainloop()
