from tkinter import *
from PIL import Image, ImageTk
from tkinter import ttk
import mysql.connector
import random
from tkinter import messagebox
from datetime import datetime



class Details:
    def __init__(self, root):
        self.root = root
        self.root.title("Hotel Management System")
        self.root.geometry("1150x530+200+200")
        
        self.var_floor=StringVar()
        self.var_roomno=StringVar()
        self.var_roomType=StringVar()
        
        
          # title
        lbl_title =Label(self.root,text="ROOM REGISTER BOOK",font=("time new roman",15,"bold"),bg="black",fg="gold",bd=2,relief=RIDGE)
        lbl_title.place(x=0,y=0,width=1150,height=40) 
        
            # labl frame 
        label_room_Left=LabelFrame(self.root,bd=1,relief=RIDGE,text="Room Adding Details",font=("time new roman",9,"bold"),padx=3,)
        label_room_Left.place(x=2,y=40,width=470,height=370) 
        
        # floor
        lbl_floor=Label(label_room_Left,text="Floor",font=("times new roman",10,"bold"), padx=1,pady=4)
        lbl_floor.grid(row=5,column=0)
        
        entry_floor=ttk.Entry(label_room_Left,width=25,textvariable=self.var_floor,font=("times new roman",10,"bold"))
        entry_floor.grid(row=5,column=1)
        
          # room no 
        lbl_roomno=Label(label_room_Left,text="Room No",font=("arial",10,"bold"), padx=1,pady=4)
        lbl_roomno.grid(row=6,column=0)
        
        entry_roomno=ttk.Entry(label_room_Left,width=25,textvariable=self.var_roomno,font=("arial",10,"bold"))
        entry_roomno.grid(row=6,column=1)
        
       
        # Room Type     
        lbl_room_type=Label(label_room_Left,text="Room Type",font=("arial",9,"bold"), padx=1,pady=4)
        lbl_room_type.grid(row=7,column=0)
        combo_room_type=ttk.Combobox(label_room_Left,textvariable=self.var_roomType,font=("arial",9,"bold"),width=23,state="readonly")
        combo_room_type["values"] = (
            "Single",
            "Double",
            "Family",
            "Luxury",
        )
        combo_room_type.current(0)
        combo_room_type.grid(row=7, column=1)
        
         # buttons 
        btn_frame=Frame(label_room_Left,bd=1,relief=RIDGE)
        btn_frame.place(x=300,y=130,width=120,height=130)
        
        btnAdd=Button(btn_frame,text="ADD",command=self.add_data, font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        btnAdd.grid(row=0,column=0,padx=1)
        
        btnUpdate=Button(btn_frame,text="UPDATE",command=self.update, font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        btnUpdate.grid(row=1,column=0,padx=1)
        
        btnDelete=Button(btn_frame,text="DELETE",command=self.delete_the_details,font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        btnDelete.grid(row=2,column=0,padx=1)
        
        btnRESET=Button(btn_frame,text="RESET",command=self.reset,font=("arial",11,"bold"),bg="black",fg="gold",width=12)
        btnRESET.grid(row=3,column=0,padx=1)
        
        # room image in side the frame 
        img0=Image.open(r"F:\Hotel Managemant system\images\images (2).jpeg")
        img0=img0.resize((195,117),Image.Resampling.LANCZOS)
        self.photoimg0=ImageTk.PhotoImage(img0)
        
    
        lbling=Label(label_room_Left,image=self.photoimg0,bd=0,relief=RIDGE)
        lbling.place(x=265,y=0,width=195,height=117)
        
        #  image in side the frame 
        img01=Image.open(r"F:\Hotel Managemant system\images\images (3).jpeg")
        img01=img01.resize((250,250),Image.Resampling.LANCZOS)
        self.photoimg01=ImageTk.PhotoImage(img01)
        
    
        lbling=Label(label_room_Left,image=self.photoimg01,bd=0,relief=RIDGE)
        lbling.place(x=0,y=100,width=250,height=250)


         # paris image 
        img10=Image.open(r"F:\Hotel Managemant system\images\paris logo.jpeg")
        img10=img10.resize((470,117),Image.Resampling.LANCZOS)
        self.photoimg10=ImageTk.PhotoImage(img10)
        
    
        lbling=Label(self.root,image=self.photoimg10,bd=0,relief=RIDGE)
        lbling.place(x=0,y=410,width=470,height=117)
        
        table_Frame=LabelFrame(self.root,bd=2,relief=RIDGE,text="Room Register Book ",font=("arial",13,"bold"),padx=2)
        table_Frame.place(x=452,y=50,width=658,height=577)
        
           # show data table
        
        room_table=Frame(table_Frame,bd=2, relief=RIDGE)
        room_table.place(x=0,y=10,width=650,height=380)
        
        scroll_x=ttk.Scrollbar(room_table,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(room_table,orient=VERTICAL)
        
        self.room_detail_table=ttk.Treeview(room_table,column=("floor", "roomno","roomtype"),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.room_detail_table.xview)
        scroll_y.config(command=self.room_detail_table.yview)
      
        self.room_detail_table.heading("floor",text="Floor")
        self.room_detail_table.heading("roomno",text="Roomno")
        self.room_detail_table.heading("roomtype",text="RoomType")
        
        
        
        self.room_detail_table["show"]="headings"
        
        self.room_detail_table.column("floor",width=100)
        self.room_detail_table.column("roomno",width=100)
        self.room_detail_table.column("roomtype",width=100)

        
        self.room_detail_table.pack(fill=BOTH,expand=1)
        self.room_detail_table.bind("<ButtonRelease-1>",self.get_cursor)
        self.fetch_data()
        
        # add data
        
    def add_data(self):
     if self.var_roomno.get() == "" :
        messagebox.showerror("Error", "All Fields are Required", parent=self.root)
     else:
        try:
            conn = mysql.connector.connect(host="localhost", username="root", password="Amit@1234", database='hms')
            cur = conn.cursor()
            cur.execute("INSERT INTO details VALUES (%s, %s, %s)",
                         (self.var_floor.get(), self.var_roomno.get(), self.var_roomType.get()))
    
            conn.commit()
            self.fetch_data()
        except Exception as e:
            messagebox.showerror("Error", f"Error occurred: {str(e)}", parent=self.root)


    def fetch_data(self):
        conn = mysql.connector.connect(host="localhost", username="root", password="Amit@1234", database='hms')
        cur = conn.cursor()
        cur.execute("SELECT * FROM details")
        rows = cur.fetchall()

        if len(rows) != 0:
            self.room_detail_table.delete(*self.room_detail_table.get_children())
            for row in rows:
                self.room_detail_table.insert("", END, values=row)
        conn.close()
        
    def get_cursor(self,event=""):
        cursor_row=self.room_detail_table.focus()
        content=self.room_detail_table.item(cursor_row)
        row=content["values"]
        
        self.var_floor.set(row[0])
        self.var_roomno.set(row[1])
        self.var_roomType.set(row[2])
       

       
    def update(self):
        if self.var_roomno.get() == "":
            messagebox.showerror("Error","Please Enter the Room number", parent=self.root)
        else:
            conn = mysql.connector.connect(host="localhost", username="root", password="Amit@1234", database='hms')
            cur = conn.cursor()
            cur.execute("UPDATE details SET Floor=%s, RoomType=%s WHERE RoomNo=%s",
                                 (self.var_floor.get(), self.var_roomType.get(), self.var_roomno.get()))


            
            conn.commit()  
            self.fetch_data()
            conn.close()
            messagebox.showinfo("Success", "Details has been updated Successfully", parent=self.root )
            
    def delete_the_details(self):
        delete_the_details = messagebox.askyesno("Hotel Management System", "Do you want to delete this customer's details", parent=self.root)
        if delete_the_details > 0:
            conn = mysql.connector.connect(host="localhost", username="root", password="Amit@1234", database='hms')
            cur = conn.cursor()
            query = "DELETE FROM details WHERE Roomno=%s"  # Corrected query
            value = (self.var_roomno.get(),)
            cur.execute(query, value)
        else:
            if not delete_the_details:
                return
        conn.commit()
        self.fetch_data()
        conn.close()
        
    def reset(self):
        self.var_floor.set("")
        self.var_roomno.set("")
        self.var_roomType.set("")

        
      

        
        
   
         




if __name__ == "__main__":
    root=Tk()
    object=Details(root)
    root.mainloop()