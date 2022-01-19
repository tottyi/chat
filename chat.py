from tkinter import *
import tkinter
import mysql.connector
import threading
import continuous_threading
import time

canvas = tkinter.Canvas(width=600, height=400)
canvas.pack()

#Databasa------------------------------------------------------------------

def db():
    global mydb, mycursor
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password="root",
      database="chat"
    )
    mycursor = mydb.cursor()

db()

def closedb():
  mycursor.close()
  mydb.close()

def chat_db():
  global chat
  mycursor.execute("SELECT login_n_from, login_n_for, text FROM chat")
  chat = mycursor.fetchall()

def data_db():
  global data
  mycursor.execute("SELECT f_name, l_name, login_name, login_passw FROM user")
  data = mycursor.fetchall()
  closedb()

data_db()

def connect():
    global myresult
    mycursor = mydb.cursor()
    mycursor.execute("SELECT login_n_from, login_n_for, text FROM chat")
    myresult = mycursor.fetchall()

# Registracia ---------------------------------------------------------------

class RegisterUser:
  def __init__(self, f_name, l_name, login, password):
    self.f_name = f_name
    self.l_name = l_name
    self.login = login
    self.password = password
    
    self.temp = temp = ['meno', 'priezvisko', 'login', 'password']
  
  def control(self):
    self.f_name
    self.l_name
    self.login
    self.password
    db()
    sql = "INSERT INTO user (f_name, l_name, login_name, login_passw) VALUES (%s,%s,%s,%s)"
    val = (self.f_name, self.l_name, self.login, self.password)
    mycursor.execute(sql, val)
    mydb.commit()
    data_db()
    print('Register sucessful', data)
    
    

def user_reg(event=None):
    p1 = RegisterUser(e5.get(), e6.get(), e7.get(), e8.get() )
    p1.control()

# LOGIN ---------------------------------------------------------------------

class Login:
  def __init__(self, login, passwd):
    self.login = login
    self.passwd = passwd
    self.temp = temp = ['meno','heslo']
  
  def control(self):
    self.login
    self.passwd
    i = 0
    for i in range(len(data)):
      if self.login == data[i][2]:
        self.temp = []
        self.temp.append(data[i][2])
        self.temp.append(data[i][3])
        break
            
    self.name()

  def name(self):
    if self.login == self.temp[0]:
      if self.passwd == self.temp[1]:
        global loged_in, user
        loged_in = self.login
        print('Welkome', self.login)
        clear_log(e9,e10,e11,e12)
        clear_reg(e1,e2,e3,e4,e5,e6,e7,e8)
        #canvas.create_text(40,50, text='User : ' + self.login)
        label = Label(canvas, text='User : ' + self.login )
        label.place(x=40, y=50)
        user = self.login
        userSelected.remove(user)  # EZT MEG KELL OLDANI VALAHOGY< HOGY JO LEGYEN ES MUKODJON
        button_hide()
        user_select()
        chat_enter()
      else:
        print('Bad Password')
            
    else:
      print('Bad Login')

def user_log(event=None):
    p1 = Login(e11.get(), e12.get())
    p1.control()

user = ''

#Register / Login Buttons & Entrys-----------------------------------------------------

e1 = Label(canvas, text="Meno :" )
e1.place(x=5, y=40)
e2 = Label(canvas, text="Priezvisko :")
e2.place(x=5, y=67)
e3 = Label(canvas, text="Login Name :" )
e3.place(x=5, y=94)
e4 = Label(canvas, text="Password :")
e4.place(x=5, y=121)
e5 = Entry(canvas, width=16) # Meno
e5.bind('<Return>', user_reg) 
e5.place(x=85, y=40)
e6 = Entry(canvas, width=16) # Priezvisko
e6.bind('<Return>', user_reg) 
e6.place(x=85, y=67)
e7 = Entry(canvas, width=16) # Login Name
e7.bind('<Return>', user_reg) 
e7.place(x=85, y=94)
e8 = Entry(canvas, width=16, show='*') # Password
e8.bind('<Return>', user_reg) 
e8.place(x=85, y=121)


def register2(x1,x2,x3,x4,x5,x6,x7,x8):
    clear_log(e9,e10,e11,e12)
    x1.place(x=5, y=40)
    x2.place(x=5, y=67)
    x3.place(x=5, y=94)
    x4.place(x=5, y=121)
    x5.place(x=85, y=40)
    x6.place(x=85, y=67)
    x7.place(x=85, y=94)
    x8.place(x=85, y=121)
    canvas.create_text(85,160, text='Press Enter for registracion')

def clear_reg(x1,x2,x3,x4,x5,x6,x7,x8):
    x1.place_forget()
    x2.place_forget()
    x3.place_forget()
    x4.place_forget()
    x5.place_forget()
    x6.place_forget()
    x7.place_forget()
    x8.place_forget()
    canvas.delete('all')

clear_reg(e1,e2,e3,e4,e5,e6,e7,e8)

e9 = Label(canvas, text="Login :" )
e9.place(x=5, y=40)
e10 = Label(canvas, text="Password")
e10.place(x=5, y=67)
e11 = Entry(canvas, width=16)            # Login
e11.bind('<Return>', user_log)         # Press Enter for Get
e11.place(x=85, y=40)
e12 = Entry(canvas, width=16, show='*')  # Password
e12.bind('<Return>', user_log)         # Press Enter for Get
e12.place(x=85, y=67)
 
def login2(x1,x2,x3,x4):
    userSelect()
    clear_reg(e1,e2,e3,e4,e5,e6,e7,e8)
    x1.place(x=5, y=40)
    x2.place(x=5, y=67)
    x3.place(x=85, y=40)
    x4.place(x=85, y=67)
    canvas.create_text(85,105, text='Press Enter for login')

def clear_log(x9,x10,x11,x12):
    x9.place_forget()
    x10.place_forget()
    x11.place_forget()
    x12.place_forget()
    canvas.delete('all')

clear_log(e9,e10,e11,e12)

#------------------------------------------------------------------------------

def buttons():
    global button1, button2
    button1 = Button(canvas, text="User Register", command= lambda: register2(e1,e2,e3,e4,e5,e6,e7,e8) )
    button1.place(x=2, y=2, height = 30, width = 80)
    button2 = Button(canvas, text="User Login", command= lambda: login2(e9,e10,e11,e12) )
    button2.place(x=82, y=2, height = 30, width = 80)

buttons()

def button_hide():
  button1.place_forget()
  button2.place_forget()

# Chat Entry -----------------------------------------------------------------

chat_data = ''

def chat_enter():
    global chat_entry
    chat_entry = Entry(canvas, width=16) # write
    chat_entry.bind('<Return>', write)
    chat_entry.place(x=5, y=80)
    maxchar = Label(canvas, text='Max. char.  20')
    maxchar.place(x=5, y=105)

def write(event=None):
    user2 = userFor
    db()
    sql = "INSERT INTO chat (login_n_from, login_n_for, text ) VALUES (%s,%s,%s)"
    val = (user, user2, chat_entry.get())
    mycursor.execute(sql, val)
    mydb.commit()
    chat_entry.delete(0, 'end')
    closedb()


# User Select Menu-----------------------------------------------------------

userSelected = []

def userSelect():
    db()
    mycursor.execute("SELECT login_name FROM user")
    xx = mycursor.fetchall()
    userSelected.clear()
    for i in range(len(xx)):
        print(xx[i][0])
        userSelected.append(xx[i][0])
    closedb()

userSelect()

variable = StringVar()

variable.set(userSelected[0])

def user_select():
  dropdown = OptionMenu( canvas, variable, *userSelected, command= user_for )
  dropdown.place(x=2, y=2, height=33, width=150)

userFor = ''

def user_for(ize):
  global userFor
  ize = variable.get()
  userFor = ize
  start1()
  #start1()

# Robot, Show always 1 sec post ----------------------------------------------

def connect():
    global myconnect
    mycursor = mydb.cursor()
    mycursor.execute("SELECT login_n_from, login_n_for, text FROM chat")
    myconnect = mycursor.fetchall()
    closedb()

def show1():
    global h, g
    h = ['']
    g = ['']
    canvas.delete('all')
    for i in range(len(myconnect)):
        if user == myconnect[i][0] and userFor == myconnect[i][1]:
            #h = ['***']
            h.append(myconnect[i][2])
    canvas.create_text(350, 20, text= user + ' : ' + h[-1], anchor=NW)
    for i in range(len(myconnect)):
        if 'pani' == myconnect[i][0] and user == myconnect[i][1]:
            #g = []
            g.append(myconnect[i][2])
    canvas.create_text(350, 35, text= userFor + ' : ' + g[-1], anchor=NW)


def start1():
    thread1.start()
    time.sleep(0.1)

def show_post1():
    while True:
        time.sleep(1)
        db()
        connect()
        show1()
        break

thread1 = continuous_threading.PausableThread(target=show_post1)
#thread.start()

canvas.mainloop()
