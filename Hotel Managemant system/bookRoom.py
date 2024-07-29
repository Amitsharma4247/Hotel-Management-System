from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from datetime import datetime



class Room_Booking:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1150x530+200+200")

                # logo Image
        img1=Image.open(r"F:\Hotel Managemant system\images\logoparis.png")
        img1=img1.resize((70,40),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lbling=Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        lbling.place(x=0,y=0,width=70,height=40)
        
        # variables
        self.var_contact=StringVar()
        self.var_checkin=StringVar()
        self.var_checkout=StringVar()
        self.var_roomtype=StringVar()
        self.var_roomavailable=StringVar()
        self.var_meal=StringVar()
        self.var_noofdays=StringVar()
        self.var_paidtax=StringVar()
        self.var_actualtotal=StringVar()
        self.var_total=StringVar()
          

     # title
        lbl_title =Label(self.root,text="ROOM BOOKING",font=("time new roman",15,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1150,height=40) 
        
            # labl frame 
        label_room_Left=LabelFrame(self.root,bd=1,relief=RIDGE,text="costumer Details",font=("time new roman",9,"bold"),padx=3,)
        label_room_Left.place(x=2,y=40,width=370,height=370) 
            
         # customer contact             
        lbl_cust_contact=Label(label_room_Left,text="Customer Contact",font=("times new roman",10,"bold"), padx=1,pady=4)
        lbl_cust_contact.grid(row=0,column=0,sticky=W)
        
        entry_contact=ttk.Entry(label_room_Left,width=22,textvariable=self.var_contact,font=("times new roman",10,"bold"))
        entry_contact.grid(row=0,column=1,sticky=W)
        
        # fetch button
        btn_fetch_data=Button(label_room_Left,text="Fetch Data",command=self.fetch_contact, font=("arial",9,"bold"),bg="black",fg="gold",width=10)
        btn_fetch_data.place(x=275,y=0)
        
        # check in date
        lbl_check_in_date=Label(label_room_Left,text="Check-In Date",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_check_in_date.grid(row=1,column=0,sticky=W)
        
        entry_check_in_date=ttk.Entry(label_room_Left,width=34,textvariable=self.var_checkin,font=("arial",10,"bold"))
        entry_check_in_date.grid(row=1,column=1)
        
        # Check-Out Date
        lbl_check_out_date=Label(label_room_Left,text="Check-Out Date",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_check_out_date.grid(row=2,column=0,sticky=W)
        
        entry_check_out_date=ttk.Entry(label_room_Left,width=34,textvariable=self.var_checkout ,font=("arial",10,"bold"))
        entry_check_out_date.grid(row=2,column=1)
        
        # Room Type     
        lbl_room_type=Label(label_room_Left,text="Room Type",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_room_type.grid(row=3,column=0,sticky=W)
        
        conn = mysql.connector.connect(host="localhost", user="root", password="Amit@1234", database='hms')
        cur = conn.cursor()
        cur.execute("SELECT Roomtype FROM details")
        rows = cur.fetchall()
        room_types = [row[0] for row in rows]  # Extract RoomType values from the tuples
        combo_room_type = ttk.Combobox(label_room_Left, textvariable=self.var_roomtype, font=("arial", 9, "bold"), width=32, state="readonly")
        combo_room_type["value"] = room_types
        combo_room_type.current(0)
        combo_room_type.grid(row=3, column=1)
        
        # available rooms   
        lbl_available_rooms=Label(label_room_Left,text="Available Rooms",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_available_rooms.grid(row=4,column=0,sticky=W)
        
        # entry_available_rooms=ttk.Entry(label_room_Left,width=34,textvariable=self.var_roomavailable ,font=("arial",10,"bold"))
        # entry_available_rooms.grid(row=4,column=1)
        
        conn = mysql.connector.connect(host="localhost", user="root", password="Amit@1234", database='hms')
        cur = conn.cursor()
        cur.execute("SELECT Roomno FROM details")
        rows = cur.fetchall()

        combo_roomno=ttk.Combobox(label_room_Left,textvariable=self.var_roomavailable ,font=("arial",9,"bold"),width=32,state="readonly")
        combo_roomno["values"] = rows
        combo_roomno.grid(row=4, column=1)
 
        
        # meals 
        lbl_meals=Label(label_room_Left,text="Meal",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_meals.grid(row=5,column=0,sticky=W)
        
        combo_meals = ttk.Combobox(
            label_room_Left,
            textvariable=self.var_meal,
            font=("arial", 10, "bold"),
            width=32,
        )
        combo_meals["values"] = ("Breakfast", "Lunch", "Dinner", "All Three")
        combo_meals.current(0)
        combo_meals.grid(row=5, column=1)
      
        
        # entry_meals=ttk.Entry(label_room_Left,width=34,textvariable=self.var_meal ,font=("arial",10,"bold"))
        # entry_meals.grid(row=5,column=1)
        
        # no. of days   
        lbl_numberof_days=Label(label_room_Left,text="No of days",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_numberof_days.grid(row=6,column=0,sticky=W)
        
        entry_numberof_days=ttk.Entry(label_room_Left,width=34,textvariable=self.var_noofdays ,font=("arial",10,"bold"))
        entry_numberof_days.grid(row=6,column=1)
        
        # paid tax
        lbl_paid_tax=Label(label_room_Left,text="Paid tax",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_paid_tax.grid(row=7,column=0,sticky=W)
        
        entry_paid_tax=ttk.Entry(label_room_Left,width=34,textvariable=self.var_paidtax,font=("arial",10,"bold"))
        entry_paid_tax.grid(row=7,column=1)
       
        # sub total         
        lbl_sub_total=Label(label_room_Left,text="Sub Total",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_sub_total.grid(row=8,column=0,sticky=W)
        
        entry_sub_total=ttk.Entry(label_room_Left,width=34,textvariable=self.var_actualtotal,font=("arial",10,"bold"))
        entry_sub_total.grid(row=8,column=1)
        
        
        # total cost
        lbl_total_cost=Label(label_room_Left,text="Total Cost",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_total_cost.grid(row=9,column=0,sticky=W)
        
        entry_total_cost=ttk.Entry(label_room_Left,width=34,textvariable=self.var_total,font=("arial",10,"bold"))
        entry_total_cost.grid(row=9,column=1)
        
        
         # Bill Button
        btn_bill=Button(label_room_Left,text="BILL",command=self.total, font=("arial",9,"bold"),bg="black",fg="gold",width=10)
        btn_bill.place(x=20,y=285)
        
         # buttons 
        btn_frame=Frame(label_room_Left,bd=1,relief=RIDGE)
        btn_frame.place(x=0,y=320,width=363,height=35)
        
        btnAdd=Button(btn_frame,text="ADD",command=self.add_data, font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="UPDATE",command=self.update, font=("arial",11,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="DELETE",command=self.delete_the_details,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnRESET=Button(btn_frame,text="RESET",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=9)
        btnRESET.grid(row=0,column=3,padx=1)
    
        # paris image 
        img8=Image.open(r"F:\Hotel Managemant system\images\paris logo.jpeg")
        img8=img8.resize((370,117),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
    
        lbling=Label(self.root,image=self.photoimg8,bd=0,relief=RIDGE)
        lbling.place(x=0,y=410,width=370,height=117)
         
        # right side bed image 
        img_bed=Image.open(r"F:\Hotel Managemant system\images\room.jpeg")
        img_bed=img_bed.resize((470,230),Image.Resampling.LANCZOS)
        self.photoimg_bed=ImageTk.PhotoImage(img_bed)
        
    
        lbling=Label(self.root,image=self.photoimg_bed,bd=0,relief=RIDGE)
        lbling.place(x=675,y=45,width=470,height=230)
       
         # table frame customer  details and search system   
        table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System ",font=("arial",13,"bold"),padx=2)
        table_Frame.place(x=372,y=250,width=778,height=277)
        
        lbl_SearchBy = Label(table_Frame, font=("arial", 12, "bold"), text="Search By:", bg="red", fg="white")
        lbl_SearchBy.grid(row=0, column=0, sticky=W)

        self.search_var = StringVar()
        combo_SearchBY = ttk.Combobox(table_Frame, textvariable=self.search_var, font=("arial", 12, "bold"), width=22, state="readonly")
        combo_SearchBY["value"] = ("Contact", "roomno") 
        combo_SearchBY.current(0)      
        combo_SearchBY.grid(row=0, column=1, padx=2)

        self.txt_search = StringVar()
        textSearch = ttk.Entry(table_Frame, width=22, textvariable=self.txt_search, font=("arial", 12, "bold"))
        textSearch.grid(row=0, column=2, padx=2)

        btnSearch = Button(table_Frame, text="Search",command=self.search, font=("arial", 11, "bold"), bg="black", fg="gold", width=8)
        btnSearch.grid(row=0, column=3, padx=1)

        
        btnShowAll=Button(table_Frame,text="Show All",font=("arial",11,"bold"),bg="black",fg="gold",width=9)
        btnShowAll.grid(row=0,column=4,padx=1)
        
         # show data table
        
        room_table=Frame(table_Frame,bd=2, relief=RIDGE)
        room_table.place(x=0,y=50,width=770,height=180)
        
        scroll_x=ttk.Scrollbar(room_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(room_table,orient=VERTICAL)
        
        self.Cust_room_table=ttk.Treeview(room_table,column=("contact","checkin", "checkout","roomtype","roomno",
                                                                   "meal","noofdays"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Cust_room_table.xview)
        scroll_y.config(command=self.Cust_room_table.yview)
      
        self.Cust_room_table.heading("contact",text="Contact")
        self.Cust_room_table.heading("checkin",text="Check-in")
        self.Cust_room_table.heading("checkout",text="Check-out")
        self.Cust_room_table.heading("roomtype",text="Room Type")
        self.Cust_room_table.heading("roomno",text="Room_Number")
        self.Cust_room_table.heading("meal",text="Meal")
        self.Cust_room_table.heading("noofdays",text="Number of days")
        
        
        self.Cust_room_table["show"]="headings"
        
        self.Cust_room_table.column("contact",width=100)
        self.Cust_room_table.column("checkin",width=100)
        self.Cust_room_table.column("checkout",width=100)
        self.Cust_room_table.column("roomtype",width=100)
        self.Cust_room_table.column("roomno",width=100)
        self.Cust_room_table.column("meal",width=100)
        self.Cust_room_table.column("noofdays",width=100)
        
        self.Cust_room_table.pack(fill=BOTH,expand=1)
        self.Cust_room_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        # add data
        
    def add_data(self):
        if self.var_contact.get() == "" or self.var_checkin.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", user="root", password="Amit@1234", database='hms')
                cur = conn.cursor()
                cur.execute("insert into rooms values(%s,%s,%s,%s,%s,%s,%s)",
                            ( self.var_contact.get(), self.var_checkin.get(),self.var_checkout.get(),
                               self.var_roomtype.get(),  self.var_roomavailable.get(), self.var_meal.get(),
                                self.var_noofdays.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Details has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Amit@1234", database='hms')
        cur = conn.cursor()
        cur.execute("SELECT * FROM rooms")
        rows = cur.fetchall()

        if len(rows) != 0:
            self.Cust_room_table.delete(*self.Cust_room_table.get_children())
            for row in rows:
                self.Cust_room_table.insert("", END, values=row)
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_row=self.Cust_room_table.focus()
        content=self.Cust_room_table.item(cursor_row)
        row=content["values"]
        
        self.var_contact.set(row[0])
        self.var_checkin.set(row[1])
        self.var_checkout.set(row[2])
        self.var_roomtype.set(row[3])
        self.var_roomavailable.set(row[4])
        self.var_meal.set(row[5])
        self.var_noofdays.set(row[6])

       
    def update(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Please Enter the Contact number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Amit@1234", database='hms')
            cur = conn.cursor()
            cur.execute("UPDATE rooms SET checkin=%s, checkout=%s, roomtype=%s, roomno=%s, meal=%s, noofdays=%s WHERE contact=%s",  ( 
                            self.var_checkin.get(),self.var_checkout.get(),
                               self.var_roomtype.get(),  self.var_roomavailable.get(), self.var_meal.get(),
                                self.var_noofdays.get(),self.var_contact.get() 
                                ))

            
            conn.commit()  
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Details has been updated Successfully", parent=self.root )
            
    def delete_the_details(self):
        delete_the_details = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer's details", parent=self.root)
        if delete_the_details > 0:
            conn = mysql.connector.connect(host="localhost", user="root", password="Amit@1234", database='hms')
            cur = conn.cursor()
            query = "DELETE FROM rooms WHERE contact=%s"  # Corrected query
            value = (self.var_contact.get(),)
            cur.execute(query, value)
        else:
            if not delete_the_details:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    def reset(self):
        self.var_contact.set("")
        self.var_checkin.set("")
        self.var_checkout.set("")
        self.var_roomtype.set("")
        self.var_roomavailable.set("")
        self.var_meal.set("")
        self.var_noofdays.set("")
        
   
        # data fetching
        
    def fetch_contact(self):
        if self.var_contact.get()=="":
            messagebox.showerror("Error","Enter the Contact Number , itnii kya jldi hai ")    
        else:
            conn = mysql.connector.connect(host="localhost", user="root", password="Amit@1234", database='hms')
            cur = conn.cursor()
            query=("select Name from customer where Mobile=%s")
            value = (self.var_contact.get(),)
            cur.execute(query,value)
            row = cur.fetchone()
            
            if row==None:
                messagebox.showerror("Error","This contact does not exist, Shi se likh na re ",parent=self.root)
            else:
                conn.commit()
                conn.close()
                
                showDataframe=Frame(self.root,bd=4,relief=RIDGE,padx=2)
                showDataframe.place(x=380,y=45,width=275,height=170)           
        
                lblName=Label(showDataframe,text="Name:",font=("arial",10,"bold"))
                lblName.place(x=0,y=0)
                
                lbl=Label(showDataframe,text=row,font=("arial",10,"bold"))
                lbl.place(x=90,y=0)
                
                conn = mysql.connector.connect(host="localhost", user="root", password="Amit@1234", database='hms')
                cur = conn.cursor()
                query=("select Gender from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                cur.execute(query,value)
                row = cur.fetchone()
              
                lblGender=Label(showDataframe,text="Gender:",font=("arial",10,"bold"))
                lblGender.place(x=0,y=30)
                
                lbl2=Label(showDataframe,text=row,font=("arial",10,"bold"))
                lbl2.place(x=90,y=30)
                
                conn = mysql.connector.connect(host="localhost", user="root", password="Amit@1234", database='hms')
                cur = conn.cursor()
                query=("select emailid from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                cur.execute(query,value)
                row = cur.fetchone()
              
                lblEmailId=Label(showDataframe,text="Email Id:",font=("arial",10,"bold"))
                lblEmailId.place(x=0,y=60)
                
                lbl3=Label(showDataframe,text=row,font=("arial",10,"bold"))
                lbl3.place(x=90,y=60)
                
                conn = mysql.connector.connect(host="localhost", user="root", password="Amit@1234", database='hms')
                cur = conn.cursor()
                query=("select Nationality from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                cur.execute(query,value)
                row = cur.fetchone()
              
                lblNationality=Label(showDataframe,text="Nationality:",font=("arial",10,"bold"))
                lblNationality.place(x=0,y=90)
                
                lbl4=Label(showDataframe,text=row,font=("arial",10,"bold"))
                lbl4.place(x=90,y=90)
        
                conn = mysql.connector.connect(host="localhost", user="root", password="Amit@1234", database='hms')
                cur = conn.cursor()
                query=("select Address from customer where Mobile=%s")
                value = (self.var_contact.get(),)
                cur.execute(query,value)
                row = cur.fetchone()
              
                lblAddress=Label(showDataframe,text="Address:",font=("arial",10,"bold"))
                lblAddress.place(x=0,y=120)
                
                lbl5=Label(showDataframe,text=row,font=("arial",10,"bold"))
                lbl5.place(x=90,y=120)

    # search system
    def search(self):
        conn = mysql.connector.connect(host="localhost", user="root", password="Amit@1234", database='hms')
        cur = conn.cursor()
        search_column = self.search_var.get()
        search_value = self.txt_search.get()
        query = f"SELECT * FROM rooms WHERE {search_column} LIKE '%{search_value}%'"
        cur.execute(query)
        rows = cur.fetchall()

        if len(rows) != 0:
            self.Cust_room_table.delete(*self.Cust_room_table.get_children())

        for row in rows:
            self.Cust_room_table.insert("", END, values=row)

        conn.commit()
        conn.close()
            
   
    def total(self):
        inDate = self.var_checkin.get()
        outDate = self.var_checkout.get()
        
        inDay, inMonth, inYear = map(int, inDate.split('/'))
        outDay, outMonth, outYear = map(int, outDate.split('/'))
        
        inDateObj = datetime(inYear, inMonth, inDay)
        outDateObj = datetime(outYear, outMonth, outDay)
        
        self.var_noofdays.set(abs((outDateObj - inDateObj).days))
  
        if (self.var_meal.get()=="All Three" and self.var_roomtype.get()=="Luxury"):
            q1=float(1000)
            q2=float(1500)  
            q3 =float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*5.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*5.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)            

        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Luxury"):
            q1=float(300)
            q2=float(1500)  
            q3 =float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*5.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*5.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)            

            
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Luxury"):
            q1=float(500)
            q2=float(1500)  
            q3 =float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*5.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*5.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)            
            
            
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Luxury"):
            q1=float(500)
            q2=float(1500)  
            q3 =float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*5.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*5.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)            
            
        elif (self.var_meal.get()=="All There" and self.var_roomtype.get()=="Single"):
            q1=float(1000)
            q2=float(1000)  
            q3 =float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*5.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*5.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 
                       
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Single"):
            q1=float(300)
            q2=float(1000)  
            q3 =float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*5.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*5.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)   
           
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Single"):
            q1=float(500)
            q2=float(1000)  
            q3 =float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*5.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*5.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)   
           
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Single"):
            q1=float(500)
            q2=float(1000)  
            q3 =float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*5.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*5.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)   
           
        elif (self.var_meal.get()=="All There" and self.var_roomtype.get()=="Double"):
            q1=float(1000)
            q2=float(1300)  
            q3 =float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*5.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*5.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 
                       
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Double"):
            q1=float(300)
            q2=float(1300)  
            q3 =float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*5.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*5.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)   
           
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Double"):
            q1=float(500)
            q2=float(1300)  
            q3 =float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*5.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*5.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)   
           
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Double"):
            q1=float(500)
            q2=float(1300)  
            q3 =float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*5.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*5.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)   
           
        elif (self.var_meal.get()=="All There" and self.var_roomtype.get()=="Family"):
            q1=float(1000)
            q2=float(2000)  
            q3 =float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*5.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*5.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT) 
                       
        elif (self.var_meal.get()=="Breakfast" and self.var_roomtype.get()=="Family"):
            q1=float(300)
            q2=float(2000)  
            q3 =float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*5.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*5.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)   
           
        elif (self.var_meal.get()=="Lunch" and self.var_roomtype.get()=="Family"):
            q1=float(500)
            q2=float(2000)  
            q3 =float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*5.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*5.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)   
           
        elif (self.var_meal.get()=="Dinner" and self.var_roomtype.get()=="Family"):
            q1=float(500)
            q2=float(2000)  
            q3 =float(self.var_noofdays.get())
            q4=float(q1+q2)
            q5=float(q3+q4)
            Tax="Rs."+str("%.2f"%((q5)*5.1))
            ST="Rs."+str("%.2f"%((q5)))
            TT="Rs."+str("%.2f"%(q5+((q5)*5.1)))
            self.var_paidtax.set(Tax)
            self.var_actualtotal.set(ST)
            self.var_total.set(TT)   

                  
if __name__ == "__main__":
    root=Tk()
    object=Room_Booking(root)
    root.mainloop()