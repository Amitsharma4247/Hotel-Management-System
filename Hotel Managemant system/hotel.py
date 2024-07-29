from tkinter import *
from PIL import Image,ImageTk
from customer import Customer_win
from bookRoom import Room_Booking
from details import Details



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
        btn_frame.place(x=0,y=30,width=195,height=122)
       
        #customer 
        cust_btn=Button(btn_frame,text="CUSTOMER",command=self.cust_details, width=21,font=("time new roman", 11, "bold"),bg="black", fg="gold", bd=0,cursor="hand1")
        cust_btn.grid(row=0,column=0,pady=1)
      
        # room 
        cust_btn=Button(btn_frame,text="ROOM",command=self.room_details,width=21,font=("time new roman", 11, "bold"),bg="black", fg="gold", bd=0,cursor="hand1")
        cust_btn.grid(row=1,column=0,pady=1)
        
        # details
        cust_btn=Button(btn_frame,text="DETAILS",command=self.details,width=21,font=("time new roman", 11, "bold"),bg="black", fg="gold", bd=0,cursor="hand1")
        cust_btn.grid(row=2,column=0,pady=1)
      
        # # report
        # cust_btn=Button(btn_frame,text="REPORT",width=21,font=("time new roman", 11, "bold"),bg="black", fg="gold", bd=0,cursor="hand1")
        # cust_btn.grid(row=3,column=0,pady=1)
        
        # logout
        cust_btn=Button(btn_frame,text="LOGOUT",command=self.logout,width=21,font=("time new roman", 11, "bold"),bg="black", fg="gold", bd=0,cursor="hand1")
        cust_btn.grid(row=4,column=0,pady=1)
        
        # igimage
        img3=Image.open(r"F:\Hotel Managemant system\images\img1.jpg")
        img3=img3.resize((1155,565),Image.Resampling.LANCZOS)
        self.photoimg3=ImageTk.PhotoImage(img3)
        
        lbling1=Label(main_frame,image=self.photoimg3,bd=4,relief=RIDGE)
        lbling1.place(x=195,y=0,width=1155,height=565)
        
        # room
        img4=Image.open(r"F:\Hotel Managemant system\images\images (1).jpeg")
        img4=img4.resize((195,215),Image.Resampling.LANCZOS)
        self.photoimg4=ImageTk.PhotoImage(img4)
        
        lbling1=Label(main_frame,image=self.photoimg4,bd=4,relief=RIDGE)
        lbling1.place(x=0,y=160,width=195,height=215)
        
        # food
        img5=Image.open(r"F:\Hotel Managemant system\images\food.jpg")
        img5=img5.resize((195,200),Image.Resampling.LANCZOS)
        self.photoimg5=ImageTk.PhotoImage(img5)
        
        lbling1=Label(main_frame,image=self.photoimg5,bd=4,relief=RIDGE)
        lbling1.place(x=0,y=375,width=195,height=200)
        
        
    def cust_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Customer_win(self.new_window)

    def room_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Room_Booking(self.new_window)
        
    def details(self):
        self.new_window=Toplevel(self.root)
        self.app=Details(self.new_window)
        
    def logout(self):
        self.root.destroy()
        
            
if __name__ == "__main__":
    root = Tk()
    app = HotelManagementSystem(root)
    root.mainloop()
    

    