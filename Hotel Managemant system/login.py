from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector
from customer import Customer_win
from tkinter import messagebox
from datetime import datetime
from bookRoom import Room_Booking
from details import Details




def main():
    win=Tk()
    app = Login_Window(win)
    win.mainloop()

class Login_Window:
    def __init__(self, root):
        self.root = root
        self.root.title("Login")
        self.root.geometry("1350x730+0+0")

        self.bg = ImageTk.PhotoImage(file=r"F:\Hotel Managemant system\images\Taj-Hotel-Mumbai-Facts.png")

        lbl_bg = Label(self.root, image=self.bg)
        lbl_bg.place(x=0, y=0, relwidth=1, relheight=1)

        frame = Frame(self.root, bg="Black")
        frame.place(x=860, y=150, width=290, height=440)
        
        img1 = Image.open(r"F:\Hotel Managemant system\images\6681204.png")
        img1 = img1.resize((100,100),Image.Resampling.LANCZOS)
        self.photoimage1 = ImageTk.PhotoImage(img1)
        lbling1=Label(image=self.photoimage1,bg="black", borderwidth=0)
        lbling1.place(x=950,y=155,height=100)
        
        get_str=Label(frame,text="Welcome Ji!", font=("cursive", 20, "bold"), fg="white",bg="black")
        get_str.place(x=65,y=100)
        
        username = lbl=Label(frame,text="Name",font=("cursive", 12, "bold"), fg="white",bg="black")
        username.place(x=70,y=152)
    
        self.textuser = ttk.Entry(frame, font=("cursive", 15)) 
        self.textuser.place(x=45,y=180)
        
        password = lbl=Label(frame,text="Password Bhi Chahiye",font=("cursive", 12, "bold"), fg="white",bg="black")
        password.place(x=70,y=222)
        
        self.textpass = ttk.Entry(frame, font=("cursive", 15)) 
        self.textpass.place(x=45,y=250)
        
        img2 = Image.open(r"F:\Hotel Managemant system\images\usernamelogo.jpeg")
        img2 = img2.resize((22,22),Image.Resampling.LANCZOS)
        self.photoimage2 = ImageTk.PhotoImage(img2)
        lbling2=Label(image=self.photoimage2,bg="black",borderwidth=0)
        lbling2.place(x=906,y=300,width=25,height=25) 
        
        img3 = Image.open(r"F:\Hotel Managemant system\images\passwordlogo.png")
        img3 = img3.resize((22,22),Image.Resampling.LANCZOS)
        self.photoimage3 = ImageTk.PhotoImage(img3)
        lbling2=Label(image=self.photoimage3,bg="black",borderwidth=0)
        lbling2.place(x=906,y=370,width=25,height=25) 
        
        # login button
        loginbtn = Button(frame,command= self.login,text="Login",font=("cursive", 12, "bold"),bd=3,relief=RIDGE,fg="white",bg="red",activeforeground="white",activebackground="red")
        loginbtn.place(x=120,y=283,height=35)
        
        
        regbtn = Button(frame,text="Register, If New!",command =self.register_window, font=("cursive", 9, "bold"),borderwidth = 0,fg="white",bg="black",activeforeground="white",activebackground="black")
        regbtn.place(x=25,y=325,width=150)
        
        
        forgetpassbtn = Button(frame,text="Passwoord Bhul gye!",command=self.forgot_password_window,font=("cursive", 9, "bold"),borderwidth = 0,fg="white",bg="black",activeforeground="white",activebackground="black")
        forgetpassbtn.place(x=30,y=345,width=150)
        
    def register_window(self):
        self.new_window=Toplevel(self.root)
        self.app=Registration(self.new_window)
        
    
    def login(self):
      if self.textuser.get() == "" or self.textpass.get() == "":
        messagebox.showerror("Error", "Pehle fill to kro itni kya jaldi h")
    
      elif self.textuser.get() == "PiZone" and self.textpass.get() == "1234":
        messagebox.showinfo("Success", "Aaiye, aapka swaagat hai")
    
      else:
        connmysql = mysql.connector.connect(host="localhost", user="root", password="Amit@1234", database='hms')
        cur = connmysql.cursor()
        
        cur.execute("SELECT * FROM register WHERE emailid=%s AND password=%s", (self.textuser.get(), self.textpass.get()))
        row = cur.fetchone()
        
        if row is None:
            messagebox.showerror("Error", "Invalid Username & password")
        else:
            open_main = messagebox.askyesno("YesNo", "Access only Admin")
            if open_main:
                self.new_window = Toplevel(self.root)
                self.app = HotelManagementSystem(self.new_window)
            else:
                return

        
        connmysql.commit()
        connmysql.close()
        
        
    def reset_pass(self):
        if self.selcombo_sec.get()=="Select":
            messagebox.showerror("Error","Select Security Question")
    
        elif self.secans.get()=="":
            messagebox.showerror("Error","Please enter the Answer")
    
        elif self.new_password.get()=="":
            messagebox.showerror("Error","Please enter the new password")
        else:
             connmysql = mysql.connector.connect(host="localhost", user="root", password="Amit@1234", database='hms')
             cur = connmysql.cursor()  
             query= ("select * from register where emailid=%s and selsecque=%s and secans=%s")
             value=(self.textuser.get(),self.selcombo_sec.get(),self.secans.get())
             cur.execute(query,value)
             row=cur.fetchone()
             if row==None:
                 messagebox.showerror("Error" ,"Please enter the correct Answers")
                
             else:
                 query=("update register set password=%s where emailid=%s")
                 value=(self.new_password.get(),self.textuser.get())
                 cur.execute(query,value)
                 
        connmysql.commit()
        connmysql.close()
        messagebox.showinfo("Information","Your password has been reseted, please Log in with new password")         
                    
    def forgot_password_window(self):
        if self.textuser.get()=="":
            messagebox.showerror("Error","Please Enter the Email Id to Reset Password") 
        else:
             connmysql = mysql.connector.connect(host="localhost", user="root", password="Amit@1234", database='hms')
             cur = connmysql.cursor()
             query=("select * from register where emailid=%s")
             value=(self.textuser.get(),)
             cur.execute(query,value)
             row=cur.fetchone()
            #  print(row)
            
            
             if row==None:
                 messagebox.showerror("Error", "Please enter the valid user name")
             else:
                 connmysql.close()
                 
                 self.root2 = Toplevel()
                 self.root2.title("Forgot Password")
                 self.root2.geometry("300x420+855+175")
                 background_color = None  # Set the desired background color

                 label_forpass = Label(self.root2, text="Password Bhul gye!", font=("times new roman", 15, "bold"), fg="red", bg="black")
                 label_forpass.place(x=0, y=10,relwidth=1)

                 # Select security Questions
                 selsecque = Label(self.root2, text="Select Security Question", font=("times new roman", 15, "bold"), bg=background_color, highlightbackground=background_color)
                 selsecque.place(x=20, y=60)

                 self.selcombo_sec = ttk.Combobox(self.root2, font=("times new roman", 15, "bold"), state="readonly")
                 self.selcombo_sec["values"] = ("Select", "Your Birth Place", "Your Nickname", "Your Favourite Movie", "Your Favourite Novel")
                 self.selcombo_sec.place(x=20, y=100, width=260)

                    # Security answer
                 secans = Label(self.root2, text="Security Answer", font=("times new roman", 15, "bold"), bg=background_color, highlightbackground=background_color)
                 secans.place(x=20, y=150)

                 self.secans = ttk.Entry(self.root2, font=("times new roman", 15))
                 self.secans.place(x=20, y=180, width=260)

                    # Password
                 new_password = Label(self.root2, text="New Password", font=("times new roman", 15, "bold"), bg=background_color, highlightbackground=background_color)
                 new_password.place(x=20, y=230)

                 self.new_password = ttk.Entry(self.root2, font=("times new roman", 15))
                 self.new_password.place(x=20, y=260, width=260)

                 btn = Button(self.root2,command=self.reset_pass, text="Reset Password",bg="green")
                 btn.place(x=100, y=330)  


                 

class Registration:
     def __init__(self, root):
        self.root = root
        self.root.title("Registration")
        self.root.geometry("1350x730+0+0")
        
        
        
        # veraible
        self.var_fname=StringVar()
        self.var_lname=StringVar()
        self.var_contact=StringVar()
        self.var_email=StringVar()
        self.var_secque=StringVar()
        self.var_secans=StringVar()
        self.var_pass=StringVar()
        self.var_conpass=StringVar()
        self.var_chkbks=IntVar()
        
        self.bg = ImageTk.PhotoImage(file=r"F:\Hotel Managemant system\images\registerImage.png")
        
        bg_lbl = Label(self.root,image=self.bg)
        bg_lbl.place(x=0,y=0,relheight=1,relwidth=1)
        

        self.bg1 = ImageTk.PhotoImage(file=r"F:\Hotel Managemant system\images\regleft.png")
        
        bgleft_lbl = Label(self.root,image=self.bg1)
        bgleft_lbl.place(x=50,y=100,height=520,width=420)

        frame = Frame(self.root,bg="White")
        frame.place(x=465,y=100,width=700,height=520)
        
        register_lbl =Label(frame,text="REGISTER KRE!",font=("times new roman",20,"bold"),fg = "red",bg="white")
        register_lbl.place(x=20,y=20)
        
        fname =Label(frame,text="First Name",font=("times new roman",15,"bold"),bg="white")
        fname.place(x=30,y=80)
        
        self.fname= ttk.Entry(frame,textvariable=self.var_fname, font=("times new roman", 15,)) 
        self.fname.place(x=30,y=110,width=235)
        
        # last name
        lname =Label(frame,text="Last Name",font=("times new roman",15,"bold"),bg="white")
        lname.place(x=360,y=80)
        
        self.lname= ttk.Entry(frame,textvariable=self.var_lname, font=("times new roman", 15,)) 
        self.lname.place(x=360,y=110,width=235)
        
        # contect number
        contact =Label(frame,text="Contact No.",font=("times new roman",15,"bold"),bg="white")
        contact.place(x=30,y=150)
        
        self.contact= ttk.Entry(frame,textvariable=self.var_contact, font=("times new roman", 15,)) 
        self.contact.place(x=30,y=180,width=235)
        
        # email id
        emailid =Label(frame,text="Email-id",font=("times new roman",15,"bold"),bg="white")
        emailid.place(x=360,y=150)
        
        self.emailid= ttk.Entry(frame,textvariable=self.var_email, font=("times new roman", 15,)) 
        self.emailid.place(x=360,y=180,width=235)
        
        # select security Questions
        selsecque =Label(frame,text="Select Security Question",font=("times new roman",15,"bold"),bg="white")
        selsecque.place(x=30,y=220)
        
        # self.fname= ttk.Entry(frame, font=("times new roman", 15,"bold")) 
        # self.fname.place(x=30,y=250,width=220)
        self.selcombo_sec =ttk.Combobox(frame,textvariable=self.var_secque, font=("times new roman",15,"bold"),state="readonly")
        self.selcombo_sec["values"] = ("Select","Your Birth Place", "Your Nik Name","Your Fevourite Movie","Your Fevourite Novel")
        self.selcombo_sec.place(x=30,y=250,width=235)
        self.selcombo_sec.current(0)
        
        
        
        # security answer
        secans =Label(frame,text="Security Answer",font=("times new roman",15,"bold"),bg="white")
        secans.place(x=360,y=220)
        
        self.secans= ttk.Entry(frame,textvariable=self.var_secans, font=("times new roman", 15,)) 
        self.secans.place(x=360,y=250,width=235)
        
        # passwoed  
        password =Label(frame,text="Password",font=("times new roman",15,"bold"),bg="white")
        password.place(x=30,y=290)
        
        self.password= ttk.Entry(frame,textvariable=self.var_pass, font=("times new roman", 15,)) 
        self.password.place(x=30,y=320,width=235)
        
        # Confirm Password
        conpass =Label(frame,text="Confirm Password",font=("times new roman",15,"bold"),bg="white")
        conpass.place(x=360,y=290)
        
        self.conpass= ttk.Entry(frame,textvariable=self.var_conpass, font=("times new roman", 15,)) 
        self.conpass.place(x=360,y=320,width=235)
        
        # check button
        checkbtn=Checkbutton(frame,variable=self.var_chkbks,text="I agree the terms and conditons",font=("times new roman", 12,"bold"),bg="white",onvalue=1,offvalue=0)
        checkbtn.place(x=50,y=360)
        
        # buttons register
        image2=Image.open(r"F:\Hotel Managemant system\images\register-button-png-18457.png")
        image2=image2.resize((80,50),Image.Resampling.LANCZOS)
        self.photoimage=ImageTk.PhotoImage(image2)
        b1 = Button(frame,image=self.photoimage, command=self.register_data,borderwidth=0,cursor="hand2")
        b1.place(x=170,y=400,width=80 )
        
        image3=Image.open(r"F:\Hotel Managemant system\images\login-button-png-18016.png")
        image3=image3.resize((100,70),Image.Resampling.LANCZOS)
        self.photoimage1=ImageTk.PhotoImage(image3)
        b2 = Button(frame,image=self.photoimage1,bg="white",border=0,cursor="hand2")
        b2.place(x=370,y=400,width=100 )
        
        
        # FUNCTION DECELARATION
     def  register_data(self):
        if self.var_fname.get()=="" or self.var_email.get()=="" or self.var_secque.get()=="Select":
            messagebox.showerror("Error","All fileds are required")
            
        elif self.var_pass.get()!= self.var_conpass.get():
            messagebox.showerror("Error", "Passwords are not matching")
            
        elif self.var_chkbks.get()==0:
            messagebox.showerror("error","Please agree our terms and conditons")
                
        else:
                # messagebox.showinfo("success","welcome Ji!")
                connmysql =mysql.connector.connect(host="localhost", user="root",password="Amit@1234", database='hms')
                cur =connmysql.cursor()
                query=("select * from register where emailid=%s")
                value = (self.var_email.get(),)
                cur.execute(query,value)
                row=cur.fetchone()
                if row!=None:
                    messagebox.showerror("Error","User already exist, Please try another email")
                else:
                    cur.execute("insert into register values(%s,%s,%s,%s,%s,%s,%s)",(
                                                                                     self.var_fname.get(),
                                                                                     self.var_lname.get(),
                                                                                     self.var_contact.get(),
                                                                                     self.var_email.get(),
                                                                                     self.var_secque.get(),
                                                                                     self.var_secans.get(),
                                                                                     self.var_pass.get()
                             
                                                                                    ))
                connmysql.commit()
                connmysql.close()
                messagebox.showinfo("Success","Registered Successfully") 
# if __name__ == "__main__":
    # root = Tk()
    # app = Registration(root)
    # root.mainloop()
    
class HotelManagementSystem:
    def __init__(self,root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry(("1350x730+0+0"))
        
        
        # image 1 
        img1=Image.open(r"F:\Hotel Managemant system\images\images.jpeg")
        img1=img1.resize((1350,125),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lbling=Label(self.root,image=self.photoimg1,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=1350,height=125)
        
        # image 2
        img2=Image.open(r"F:\Hotel Managemant system\images\logoparis.png")
        img2=img2.resize((195,125),Image.Resampling.LANCZOS)
        self.photoimg2=ImageTk.PhotoImage(img2)
        
        lbling=Label(self.root,image=self.photoimg2,bd=4,relief=RIDGE)
        lbling.place(x=0,y=0,width=195,height=125)
        
        # title
        lbl_title =Label(self.root,text="HOTEL PARIS",font=("time new roman",35,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
        lbl_title.place(x=0,y=125,width=1350,height=40)    
        
        # frame
        main_frame=Frame(self.root,bd=2,relief=RIDGE)
        main_frame.place(x=0,y=165,width=1550,height=565)
        
        # menu
        lbl_menu = Label(main_frame, text="MENU", font=("time new roman", 15, "bold"), bg="black", fg="gold", bd=2, relief=RIDGE)
        lbl_menu.place(x=0,y=0,width=195)    
        
        #  button frame
        btn_frame=Frame(main_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=30,width=195,height=150)
       
        #customer 
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details, width=21,font=("time new roman", 11, "bold"),bg="black", fg="gold", bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)
      
        # room 
        cust_btn=Button(btn_frame,text="ROOM",width=21,font=("time new roman", 11, "bold"),bg="black", fg="gold", bd=0,cursor="hand1")
        cust_btn.grid(row=1,column=0,pady=1)
        
        # detals
        cust_btn=Button(btn_frame,text="DETAILS",width=21,font=("time new roman", 11, "bold"),bg="black", fg="gold", bd=0,cursor="hand1")
        cust_btn.grid(row=2,column=0,pady=1)
      
        # report
        cust_btn=Button(btn_frame,text="REPORT",width=21,font=("time new roman", 11, "bold"),bg="black", fg="gold", bd=0,cursor="hand1")
        cust_btn.grid(row=3,column=0,pady=1)
        
        # logout
        cust_btn=Button(btn_frame,text="LOGOUT",width=21,font=("time new roman", 11, "bold"),bg="black", fg="gold", bd=0,cursor="hand1")
        cust_btn.grid(row=4,column=0,pady=1)
        
        # igimage
        img3=Image.open(r"F:\Hotel Managemant system\images\img1.jpg")
        img3=img3.resize((1155,565),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lbling1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lbling1.place(x=195,y=0,width=1155,height=565)
        
        # room
        img4=Image.open(r"F:\Hotel Managemant system\images\images (1).jpeg")
        img4=img4.resize((195,195),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        lbling1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lbling1.place(x=0,y=180,width=195,height=195)
        
        # food
        img5=Image.open(r"F:\Hotel Managemant system\images\food.jpg")
        img5=img5.resize((195,200),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        lbling1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lbling1.place(x=0,y=375,width=195,height=200)
        
        
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Customer_win(self.new_window)

# if __name__ == "__main__":
    # root = Tk()
    # app = HotelManagementSystem(root)
    # root.mainloop()
    

    

   
   
if __name__ == "__main__":
    main()
    # root = Tk()
    # app = Login_Window(root)
    # root.mainloop()
