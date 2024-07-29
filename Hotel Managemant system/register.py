from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import mysql.connector


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
                connmysql =mysql.connector.connect(host="localhost", username="root",password="Amit@1234", database='hms')
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
if __name__ == "__main__":
    root = Tk()
    app = Registration(root)
    root.mainloop()
