from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import random
import mysql.connector
from tkinter import messagebox


class Customer_win:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1150x530+200+200")

        self.var_ref = StringVar()
        x = random.randint(1000, 9999)
        self.var_ref.set(str(x))        
        self.var_cust_name=StringVar()
        self.var_mother=StringVar()
        self.var_gender=StringVar()
        self.var_postal=StringVar()
        self.var_mobile=StringVar()
        self.var_email=StringVar()
        self.var_nationality=StringVar()
        self.var_id_proof=StringVar()
        self.var_id_num=StringVar()
        self.var_address=StringVar()
        
        
          # title
        lbl_title =Label(self.root,text="ADD CUSTOMER DETAILS",font=("time new roman",13,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1150,height=40)   
        
        # logo Image
        img1=Image.open(r"F:\Projects PiZone\python projects\Hotel Managemant system\images\logoparis.png")
        img1=img1.resize((70,40),Image.Resampling.LANCZOS)
        self.photoimg1=ImageTk.PhotoImage(img1)
        
        lbling=Label(self.root,image=self.photoimg1,bd=0,relief=RIDGE)
        lbling.place(x=0,y=0,width=70,height=40)
        
        # labl frame 
        label_Left=LabelFrame(self.root,bd=1,relief=RIDGE,text="costumer Details",font=("time new roman",9,"bold"),padx=3,)
        label_Left.place(x=2,y=40,width=370,height=370) 
        
        # labels and entry
        lbl_cust_ref=Label(label_Left,text="Customer Ref",font=("times new roman",10,"bold"), padx=1,pady=4)
        lbl_cust_ref.grid(row=0,column=0,sticky=W)
        
        entry_ref=ttk.Entry(label_Left,width=30,textvariable=self.var_ref,font=("times new roman",10,"bold"),state="readonly")
        entry_ref.grid(row=0,column=1)
        
        # customer name
        lbl_cust_Name=Label(label_Left,text="Customer Name",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_cust_Name.grid(row=1,column=0,sticky=W)
        
        entry_ref=ttk.Entry(label_Left,width=30,textvariable=self.var_cust_name,font=("arial",10,"bold"))
        entry_ref.grid(row=1,column=1)
        
        # mother name
        lbl_cust_Name=Label(label_Left,text="Mother Name",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_cust_Name.grid(row=2,column=0,sticky=W)
        
        entry_ref=ttk.Entry(label_Left,width=30,textvariable=self.var_mother, font=("arial",10,"bold"))
        entry_ref.grid(row=2,column=1)
        
        # gender combo box
        lbl_cust_gender=Label(label_Left,text="Gender",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_cust_gender.grid(row=3,column=0,sticky=W)
        combo_gender=ttk.Combobox(label_Left,textvariable=self.var_gender, font=("arial",9,"bold"),width=28,state="readonly")
        combo_gender["value"]=("Male","Female","Others")
        combo_gender.current(0)
        combo_gender.grid(row=3,column=1)
        
        # postal code
        lbl_postal_code=Label(label_Left,text="Postal Code",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_postal_code.grid(row=4,column=0,sticky=W)
        
        entry_ref=ttk.Entry(label_Left,width=30,textvariable=self.var_postal, font=("arial",10,"bold"))
        entry_ref.grid(row=4,column=1)
        
        # mobile no.
        lbl_mobole_no=Label(label_Left,text="Mobile No.",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_mobole_no.grid(row=5,column=0,sticky=W)
        
        entry_ref=ttk.Entry(label_Left,width=30,textvariable=self.var_mobile, font=("arial",10,"bold"))
        entry_ref.grid(row=5,column=1)
        
        # Email.
        lbl_emailid=Label(label_Left,text="Eamil Id",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_emailid.grid(row=6,column=0,sticky=W)
        
        entry_ref=ttk.Entry(label_Left,width=30,textvariable=self.var_email, font=("arial",10,"bold"))
        entry_ref.grid(row=6,column=1)
        
        # Nationality
        lbl_nationality=Label(label_Left,text="Nationality",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_nationality.grid(row=7,column=0,sticky=W)
        
        combo_nationality=ttk.Combobox(label_Left,textvariable=self.var_nationality, font=("arial",9,"bold"),width=28,state="readonly")
        combo_nationality["value"]=("Indian","French","Europian","American") 
        combo_nationality.current(0)      
        combo_nationality.grid(row=7,column=1)
        
        #  id proof type
        lbl_idproof_type=Label(label_Left,text="Id Proof",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_idproof_type.grid(row=8,column=0,sticky=W)
        
        combo_idproof_type=ttk.Combobox(label_Left,textvariable=self.var_id_proof,font=("arial",9,"bold"),width=28,state="readonly")
        combo_idproof_type["value"]=("Aadhar Card","PAN Card","Driving license") 
        combo_idproof_type.current(0)      
        combo_idproof_type.grid(row=8,column=1)
        
        # id no.
        lbl_id_no=Label(label_Left,text="Id Number",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_id_no.grid(row=9,column=0,sticky=W)
        
        entry_ref=ttk.Entry(label_Left,width=30,textvariable=self.var_id_num,font=("arial",10,"bold"))
        entry_ref.grid(row=9,column=1)
        
        # ADDRRRESS.
        lbl_address=Label(label_Left,text="Address",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_address.grid(row=10,column=0,sticky=W)
        
        entry_ref=ttk.Entry(label_Left,width=30,textvariable=self.var_address,font=("arial",10,"bold"))
        entry_ref.grid(row=10,column=1)
        
        
        # buttons 
        btn_frame=Frame(label_Left,bd=1,relief=RIDGE)
        btn_frame.place(x=0,y=315,width=363,height=40)
        
        btnAdd=Button(btn_frame,text="ADD",command=self.add_data, font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="UPDATE",font=("arial",11,"bold"),bg="black",fg="gold",width=9)
        btnUpdate.grid(row=0,column=1,padx=1)
        
        btnDelete=Button(btn_frame,text="DELETE",font=("arial",11,"bold"),bg="black",fg="gold",width=9)
        btnDelete.grid(row=0,column=2,padx=1)
        
        btnRESET=Button(btn_frame,text="RESET",font=("arial",11,"bold"),bg="black",fg="gold",width=9)
        btnRESET.grid(row=0,column=3,padx=1)
        
        
         # paris image 
        img8=Image.open(r"F:\Projects PiZone\python projects\Hotel Managemant system\images\paris logo.jpeg")
        img8=img8.resize((370,117),Image.Resampling.LANCZOS)
        self.photoimg8=ImageTk.PhotoImage(img8)
        
        # table frame
        lbling=Label(self.root,image=self.photoimg8,bd=0,relief=RIDGE)
        lbling.place(x=0,y=410,width=370,height=117)
       
        # table frame customer  details and search system   
        table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="View Details And Search System ",font=("arial",13,"bold"),padx=2)
        table_Frame.place(x=372,y=40,width=783,height=487)
        
        lbl_SearchBy=Label(table_Frame,font=("arial",12,"bold"),text="Search By:",bg="red",fg="white")
        lbl_SearchBy.grid(row=0,column=0,sticky=W)
        
        combo_SearchBY=ttk.Combobox(table_Frame,font=("arial",12,"bold"),width=22,state="readonly")
        combo_SearchBY["value"]=("Mobile No.","Ref No.") 
        combo_SearchBY.current(0)      
        combo_SearchBY.grid(row=0,column=1,padx=2)
        
        textSearch=ttk.Entry(table_Frame,width=22,font=("arial",12,"bold"))
        textSearch.grid(row=0,column=2,padx=2)
        
        btnSearch=Button(table_Frame,text="Search",font=("arial",11,"bold"),bg="black",fg="gold",width=8)
        btnSearch.grid(row=0,column=3,padx=1)
        
        btnShowAll=Button(table_Frame,text="Show All",font=("arial",11,"bold"),bg="black",fg="gold",width=9)
        btnShowAll.grid(row=0,column=4,padx=1)
        
        # show data table
        
        details_table=Frame(table_Frame,bd=2, relief=RIDGE)
        details_table.place(x=0,y=50,width=770,height=350)
        
        scroll_x=ttk.Scrollbar(details_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(details_table,orient=VERTICAL)
        
        self.Cust_details_table=ttk.Treeview(details_table,column=("ref","name", "Mother's Name","Gender","postal code","Mobile no.",
                                                                   "email Id","Nationality","Id Proof","Id Number","Address"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.Cust_details_table.xview)
        scroll_y.config(command=self.Cust_details_table.yview)
      
        self.Cust_details_table.heading("ref",text="Refer No")
        self.Cust_details_table.heading("name",text="Customer Name")
        self.Cust_details_table.heading("Mother's Name",text="Mother Name")
        self.Cust_details_table.heading("Gender",text="Gender")
        self.Cust_details_table.heading("postal code",text="Postal Code")
        self.Cust_details_table.heading("Mobile no.",text="Mobile Number")
        self.Cust_details_table.heading("email Id",text="Email Id")
        self.Cust_details_table.heading("Nationality",text="Nationality")
        self.Cust_details_table.heading("Id Proof",text="Id Proof")
        self.Cust_details_table.heading("Id Number",text="Id Number")
        self.Cust_details_table.heading("Address",text="Address")
        
        self.Cust_details_table["show"]="headings"
        
        self.Cust_details_table.column("ref",width=100)
        self.Cust_details_table.column("name",width=100)
        self.Cust_details_table.column("Mother's Name",width=100)
        self.Cust_details_table.column("Gender",width=100)
        self.Cust_details_table.column("postal code",width=100)
        self.Cust_details_table.column("Mobile no.",width=100)
        self.Cust_details_table.column("email Id",width=100)
        self.Cust_details_table.column("Nationality",width=100)
        self.Cust_details_table.column("Id Proof",width=100)
        self.Cust_details_table.column("Id Number",width=100)
        self.Cust_details_table.column("Address",width=100)
        
        self.Cust_details_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        
    def add_data(self):
        if self.var_mobile.get() == "" or self.var_mother.get() == "":
            messagebox.showerror("Error", "All Fields are Required", parent=self.root)
        else:
            try:
                conn = mysql.connector.connect(host="localhost", username="root", password="Amit@1234", database='hms')
                cur = conn.cursor()
                cur.execute("insert into customer values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",
                            (self.var_ref.get(), self.var_cust_name.get(), self.var_mother.get(),
                             self.var_gender.get(), self.var_postal.get(), self.var_mobile.get(),
                             self.var_email.get(), self.var_nationality.get(), self.var_id_proof.get(),
                             self.var_id_num.get(), self.var_address.get()))
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo("Success", "Customer has been added", parent=self.root)
            except Exception as es:
                messagebox.showwarning("Warning", f"Something went wrong: {str(es)}", parent=self.root)

    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Amit@1234", database='hms')
        cur = conn.cursor()
        cur.execute("SELECT * FROM customer")
        rows = cur.fetchall()

        if len(rows) != 0:
            self.Cust_details_table.delete(*self.Cust_details_table.get_children())
            for row in rows:
                self.Cust_details_table.insert("", END, values=row)
        conn.close()


if __name__ == "__main__":
    root = Tk()
    app = Customer_win(root)
    root.mainloop()