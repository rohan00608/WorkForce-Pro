from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter.font import BOLD
from PIL import Image,ImageTk
#import _mysql_connector
import mysql.connector


class Employee:
    #***********************************FUNCTION DECLARATION****************************************
    
    #***********************************ADDING EMPLOYEE FUNCTION************************************
    
    def add_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='1234',database='mydata')
                my_cursor=conn.cursor()
                my_cursor.execute('insert into employee values(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)',(
                    self.var_dep.get(),
                    self.var_name.get(),
                    self.var_desgination.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_married.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_idproofcomb.get(),
                    self.var_idproof.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_country.get(),
                    self.var_salary.get()
                                                                                                    ))
                conn.commit()
                self.fetch_data()
                conn.close()    
                messagebox.showinfo('Sucess','Employee has been added',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f"Due To:{str(es)}",parent=self.root)    
                    
    #******************************FETCHING Data FUNCTION***************************************************
    
    def fetch_data(self):
        conn=mysql.connector.connect(host='localhost',user='root',password='1234',database='mydata')
        my_cursor=conn.cursor()
        my_cursor.execute('select * from employee')
        data=my_cursor.fetchall()
        if len(data)!=0:
            self.employee_table.delete(*self.employee_table.get_children())
            for i in data:
                self.employee_table.insert('',END,values=i)
            conn.commit()
        conn.close()    
                
    #************************************GET CURSOR BY CLICK A DATA IN TABLE THE FIELS GET FILLED AUTOMATICALLY***********************************
    
    def get_cursor(self,event=""):
        cursor_row=self.employee_table.focus()
        content=self.employee_table.item(cursor_row)
        data=content['values'] 
        
        self.var_dep.set(data[0]),
        self.var_name.set(data[1]),
        self.var_desgination.set(data[2]),
        self.var_email.set(data[3]),
        self.var_address.set(data[4]),
        self.var_married.set(data[5]),
        self.var_dob.set(data[6]),
        self.var_doj.set(data[7]),
        self.var_idproofcomb.set(data[8]),
        self.var_idproof.set(data[9]),
        self.var_gender.set(data[10]),
        self.var_phone.set(data[11]),
        self.var_country.set(data[12]),
        self.var_salary.set(data[13])                          
    
    #************************************UPDATE FUNCTION****************************************************************
    
    def update_data(self):
        if self.var_dep.get()=="" or self.var_email.get()=="":
            messagebox.showerror('Error','All Fields are required')
        else:
            try:
                update=messagebox.askyesno('Update','Are you sure to update this employee data' )
                if update>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='1234',database='mydata')
                    my_cursor=conn.cursor()
                    my_cursor.execute('update employee set Department=%s,Name=%s,Designation=%s,Email=%s,Address=%s,Married_status=%s,DOB=%s,DOJ=%s,id_proof_type=%s,Gender=%s,Phone=%s,Country=%s,Salary=%s where id_proof=%s',(
                    self.var_dep.get(),
                    self.var_name.get(),
                    self.var_desgination.get(),
                    self.var_email.get(),
                    self.var_address.get(),
                    self.var_married.get(),
                    self.var_dob.get(),
                    self.var_doj.get(),
                    self.var_idproofcomb.get(),
                    self.var_gender.get(),
                    self.var_phone.get(),
                    self.var_country.get(),
                    self.var_salary.get(),
                    self.var_idproof.get()
                    ))
                else:
                    if not update:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('Success','Employee Successfully Updated',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f"Due To:{str(es)}",parent=self.root)  
                    
    #************************************DELETE FUNCTION***************************************************            
    
    def delete_data(self):
        if self.var_idproof.get()=="":
            messagebox.showerror('Error','All fields are required')
        else:
            try:
                delete=messagebox.askyesno('Delete','Are you sure you want to delete this employee',parent=self.root)
                if delete>0:
                    conn=mysql.connector.connect(host='localhost',user='root',password='1234',database='mydata')
                    my_cursor=conn.cursor()
                    sql='delete from employee where id_proof=%s'
                    value=(self.var_idproof.get(),)
                    my_cursor.execute(sql,value)
                else:
                    if not delete:
                        return
                conn.commit()
                self.fetch_data()
                conn.close()
                messagebox.showinfo('delete','Employee Successfully deleted.',parent=self.root)
            except Exception as es:
                messagebox.showerror('Error',f"Due To:{str(es)}",parent=self.root)          
    
    #***********************************CLEAR FUNCTION**************************************************************
    
    def reset_data(self):
        self.var_dep.set("Select Department"),
        self.var_name.set(""),
        self.var_desgination.set(""),
        self.var_email.set(""),
        self.var_address.set(""),
        self.var_married.set("Married"),
        self.var_dob.set(""),
        self.var_doj.set(""),
        self.var_idproofcomb.set("Select ID Proof"),
        self.var_idproof.set(""),
        self.var_gender.set(""),
        self.var_phone.set(""),
        self.var_country.set(""),
        self.var_salary.set("")   
        
    #********************************SEARCH FRAME FUNCTION*******************************************************
    
    #********************************* SEACRH BUTTON WALA SYNTAX NAHI SAMJH RAHA HAI TRYING INDIVIDUAL or SERACH***********************
    
    def search_data(self):
        if self.var_com_search.get()=="" or self.var_search.get()=="":
            messagebox.showerror('Error','Please select option')
        else:
            try:
                conn=mysql.connector.connect(host='localhost',user='root',password='1234',database='mydata')
                my_cursor=conn.cursor()    
                my_cursor.execute('select * from employee where ' +str(self.var_com_search.get())+" LIKE '%" +str(self.var_search.get()+"%'"))                           
                rows=my_cursor.fetchall()
                if len(rows)!=0:
                    self.employee_table.delete(*self.employee_table.get_children())
                    for i in rows:
                        self.employee_table.insert("",END,values=i)
                        conn.commit()
                        self.fetch_data()
                    conn.commit()
            except Exception as es:
                messagebox.showerror('Error',f"Due To:{str(es)}",parent=self.root)
                                                                                                                    
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790")
        self.root.title('Employee management system')
       
        #*******************VARIABLES FOR ENTRY AND COMBO BOX*******************************************
        
        self.var_dep=StringVar()
        self.var_name=StringVar()
        self.var_desgination=StringVar()
        self.var_email=StringVar()
        self.var_address=StringVar()
        self.var_married=StringVar()
        self.var_dob=StringVar()
        self.var_doj=StringVar()
        self.var_idproofcomb=StringVar()
        self.var_idproof=StringVar()
        self.var_gender=StringVar()
        self.var_phone=StringVar()
        self.var_country=StringVar()
        self.var_salary=StringVar()
        
        lbl_title=Label(self.root,text="EMPLOYEE MANAGEMENT SYSTEM",font=("times new roman",37,"bold"),fg='darkblue',bg='white')    
        lbl_title.place(x=0,y=0,width=1530,height=50)

        #***********************adding logo image near employee management system*******************************
        
        img_logo=Image.open('employees pis/employ.jpg')
        img_logo=img_logo.resize((50,50),Image.ANTIALIAS)
        self.photo_logo=ImageTk.PhotoImage(img_logo)
        
        #**************************adjusting it to fit near employee word away from x axis***************************
         
        self.logo=Label(self.root,image=self.photo_logo)  
        self.logo.place(x=270,y=0,width=50,height=50)      
        
        #************IMAGE FRAME*******************************
        
        img_frame=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        img_frame.place(x=0,y=50,width=1370,height=160)
        
        #*************************1st image out of 3*********************************************
        img1=Image.open('employees pis/employee2.jpg')
        img1=img1.resize((540,160),Image.ANTIALIAS)
        self.photo1=ImageTk.PhotoImage(img1)
        
        #*****************************adjusting of image 1*********************************
        
        self.img_1=Label(img_frame,image=self.photo1)  
        self.img_1.place(x=0,y=0,width=540,height=160)   
        
        #******************************2nd image out of 3***********************************
        
        img2=Image.open('employees pis/employee1.jpg')
        img2=img2.resize((540,160),Image.ANTIALIAS)
        self.photo2=ImageTk.PhotoImage(img2)
        
        #*********************adjusting of image 2*******************************************
        
        self.img_2=Label(img_frame,image=self.photo2)  
        self.img_2.place(x=540,y=0,width=540,height=160)  
        
        #***********************3rd image out of 3*******************************************
        img3=Image.open('employees pis/employee3.jpg')
        img3=img3.resize((540,160),Image.ANTIALIAS)
        self.photo3=ImageTk.PhotoImage(img3)
        
        #adjusting of image 3
        self.img_3=Label(img_frame,image=self.photo3)  
        self.img_3.place(x=1000,y=0,width=540,height=160)  
      
        #MAIN FRAME
        main_frame=Frame(self.root,bd=2,relief=RAISED,bg="white")
        main_frame.place(x=10,y=220,width=1340,height=485)
        
        #upper frame 
        upper_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text='Employee Information',font=("times new roman",11,"bold"),fg='red')
        upper_frame.place(x=10,y=10,width=1315,height=270)
        
        # DEPARTMENT ENTRY FIELD
        lbl_dep=Label(upper_frame,text="Department :",font=("arial",11,"bold"),bg="white")
        lbl_dep.grid(row=0,column=0,padx=2,sticky=W)
        
        combo_dep=ttk.Combobox(upper_frame,textvariable= self.var_dep,font=("airal",12,"bold"),width=17,state='readonly')
        combo_dep['value']=('Select Department','HR','Software Engineer','Manager')
        combo_dep.current(0)
        combo_dep.grid(row=0,column=1,padx=2,pady=10,sticky=W)
        
        #NAME 
        lbl_Name=Label(upper_frame,font=('arial',12,'bold'),text="Name:",bg="white")
        lbl_Name.grid(row=0,column=2,padx=2,pady=7,sticky=W)
        
        txt_Name=ttk.Entry(upper_frame,textvariable=self.var_name,width=22,font=('arial',11,'bold'))
        txt_Name.grid(row=0,column=3,padx=2,pady=7)
        
        #lbl_Desgination
        lbl_Desgination=Label(upper_frame,font=('arial',12,'bold'),text="Desgination:",bg="white")
        lbl_Desgination.grid(row=1,column=0,padx=2,pady=7,sticky=W)
        
        txt_Desgination=ttk.Entry(upper_frame,textvariable=self.var_desgination,width=22,font=('arial',11,'bold'))
        txt_Desgination.grid(row=1,column=1,padx=2,pady=7)
        
        #EMAIL
        lbl_email=Label(upper_frame,font=('arial',12,'bold'),text="Email:",bg="white")
        lbl_email.grid(row=1,column=2,padx=2,pady=7,sticky=W)
        
        txt_email=ttk.Entry(upper_frame,textvariable=self.var_email,width=22,font=('arial',11,'bold'))
        txt_email.grid(row=1,column=3,padx=2,pady=7)
        
        #ADDRESS
        lbl_address=Label(upper_frame,font=('arial',12,'bold'),text="Address:",bg="white")
        lbl_address.grid(row=2,column=0,padx=2,pady=7,sticky=W)
        
        txt_address=ttk.Entry(upper_frame,textvariable=self.var_address,width=22,font=('arial',11,'bold'))
        txt_address.grid(row=2,column=1,padx=2,pady=7)
        
        #Married
        lbl_married_status=Label(upper_frame,text="Marriage Status :",font=("arial",11,"bold"),bg="white")
        lbl_married_status.grid(row=2,column=2,padx=2,sticky=W)
        
        com_txt_married=ttk.Combobox(upper_frame,textvariable=self.var_married,font=("airal",12,"bold"),width=18,state='readonly')
        com_txt_married['value']=('Married','Unmarried')
        com_txt_married.current(0)
        com_txt_married.grid(row=2,column=3,padx=2,pady=7,sticky=W)
        
        #DOB
        lbl_dob=Label(upper_frame,font=('arial',12,'bold'),text="DOB :",bg="white")
        lbl_dob.grid(row=3,column=0,padx=2,pady=7,sticky=W)
        
        txt_dob=ttk.Entry(upper_frame,textvariable=self.var_dob,width=22,font=('arial',11,'bold'))
        txt_dob.grid(row=3,column=1,padx=2,pady=7)
        
        #DATE OF JOINING
        lbl_doj=Label(upper_frame,font=('arial',12,'bold'),text="DOJ :",bg="white")
        lbl_doj.grid(row=3,column=2,padx=2,pady=7,sticky=W)
        
        txt_doj=ttk.Entry(upper_frame,textvariable=self.var_doj,width=22,font=('arial',11,'bold'))
        txt_doj.grid(row=3,column=3,padx=2,pady=7)
       
       #ID Proof 
        com_txt_proof=ttk.Combobox(upper_frame,textvariable=self.var_idproofcomb,font=("airal",12,"bold"),width=18,state='readonly')
        com_txt_proof['value']=("Select ID Proof",'PAN CARD','ADHAR CARD','DRIVING LICENSE')
        com_txt_proof.current(0)
        com_txt_proof.grid(row=4,column=0,padx=2,pady=7,sticky=W)
       
        txt_proof=ttk.Entry(upper_frame,textvariable=self.var_idproof,width=22,font=('arial',11,'bold'))
        txt_proof.grid(row=4,column=1,padx=2,pady=7)
        
        #GENDER
        lbl_gender=Label(upper_frame,font=('arial',12,'bold'),text="GENDER :",bg="white")
        lbl_gender.grid(row=4,column=2,padx=2,pady=7,sticky=W)
        
        com_txt_gender=ttk.Combobox(upper_frame,textvariable=self.var_gender,font=("airal",12,"bold"),width=18,state='readonly')
        com_txt_gender['value']=("Select Gender",'Male',"Female","Others")
        com_txt_gender.current(0)
        com_txt_gender.grid(row=4,column=3,padx=2,pady=7,sticky=W)
        
        #PHONE NUMBER
        lbl_phone=Label(upper_frame,font=('arial',12,'bold'),text="PHONE NO :",bg="white")
        lbl_phone.grid(row=0,column=4,padx=2,pady=7,sticky=W)
        
        txt_phone=ttk.Entry(upper_frame,textvariable=self.var_phone,width=22,font=('arial',11,'bold'))
        txt_phone.grid(row=0,column=5,padx=2,pady=7)
        
        #COUNTRY
        lbl_country=Label(upper_frame,font=('arial',12,'bold'),text="COUNTRY :",bg="white")
        lbl_country.grid(row=1,column=4,padx=2,pady=7,sticky=W)
        
        txt_country=ttk.Entry(upper_frame,textvariable=self.var_country,width=22,font=('arial',11,'bold'))
        txt_country.grid(row=1,column=5,padx=2,pady=7)
        
        #SALARY(CTC)
        lbl_ctc=Label(upper_frame,font=('arial',12,'bold'),text="SALARY(CTC) :",bg="white")
        lbl_ctc.grid(row=2,column=4,padx=2,pady=7,sticky=W)
        
        txt_ctc=ttk.Entry(upper_frame,textvariable=self.var_salary,width=22,font=('arial',11,'bold'))
        txt_ctc.grid(row=2,column=5,padx=2,pady=7)
        
        #MAIN FRAME PIC 
        #img4=Image.open('employees pis/employee4.jpg')
        #img4=img4.resize((220,220),Image.ANTIALIAS)
        #self.photo4=ImageTk.PhotoImage(img4)
        
        #ADJUSTING OF MAIN FRAME IMAGE
        #self.img_4=Label(upper_frame,image=self.photo4)  
        #self.img_4.place(x=1010,y=0,width=200,height=220) 
        
        #Button FRAME
        button_frame=Frame(upper_frame,bd=2,relief=RAISED,bg="white")
        button_frame.place(x=1100,y=10,width=170,height=210)
      
        btn_add=Button(button_frame,text="SAVE",command=self.add_data,font=("airal",15,"bold"),width=10,bg='blue',fg='white')
        btn_add.grid(row=0,column=0,padx=16,pady=5)
        
        btn_update=Button(button_frame,command=self.update_data,text="UPDATE",font=("airal",15,"bold"),width=10,bg='blue',fg='white')
        btn_update.grid(row=1,column=0,padx=16,pady=5)
        
        btn_delete=Button(button_frame,command=self.delete_data,text="DELETE",font=("airal",15,"bold"),width=10,bg='blue',fg='white')
        btn_delete.grid(row=2,column=0,padx=16,pady=5)
        
        btn_clear=Button(button_frame,command=self.reset_data,text="CLEAR",font=("airal",15,"bold"),width=10,bg='blue',fg='white')
        btn_clear.grid(row=3,column=0,padx=16,pady=5)
        
        #Down Frame 
        down_frame=LabelFrame(main_frame,bd=2,relief=RIDGE,bg="white",text='Employee Information Table',font=("times new roman",11,"bold"),fg='red')
        down_frame.place(x=10,y=280,width=1315,height=195)
        
        #SEARCH FRAME
        search_frame=LabelFrame(down_frame,bd=2,relief=RIDGE,bg="white",text='Search Employee Information',font=("times new roman",11,"bold"),fg='red')
        search_frame.place(x=0,y=0,width=1310,height=60)
        
        search_by=Label(search_frame,font=('arial',12,'bold'),text="Search By :",bg="red",fg='white')
        search_by.grid(row=0,column=0,padx=5,sticky=W)
       
        #Search Frame Buttons and Labels 
        
        self.var_com_search=StringVar()
        com_txt_search=ttk.Combobox(search_frame,textvariable=self.var_com_search,font=("airal",12,"bold"),width=18,state='readonly')
        com_txt_search['value']=("Select Option",'Phone',"ID Proof")
        com_txt_search.current(0)
        com_txt_search.grid(row=0,column=1,padx=5,sticky=W)
        
        self.var_search=StringVar()
        txt_search=ttk.Entry(search_frame,textvariable=self.var_search,width=22,font=('arial',11,'bold'))
        txt_search.grid(row=0,column=2,padx=5)
        
        btn_search=Button(search_frame,command=self.search_data,text="SEARCH",font=("airal",15,"bold"),width=10,bg='blue',fg='white')
        btn_search.grid(row=0,column=3,padx=5)
        
        btn_Showall=Button(search_frame,text="Show All",command=self.fetch_data,font=("airal",15,"bold"),width=10,bg='blue',fg='white')
        btn_Showall.grid(row=0,column=4,padx=5)
        
        search_label=Label(search_frame,text="Version 1.0",font=("times new roman",27,"bold"),width=5)
        search_label.place(x=780,y=0,width=515,height=30)
        
        #adding of image in search frame
        img_logo_frame=Image.open('employees pis/search_logo.jpg')
        img_logo_frame=img_logo_frame.resize((50,50),Image.ANTIALIAS)
        self.photo_logo2=ImageTk.PhotoImage(img_logo_frame)
        
        #adjusting it to fit near logo away from x axis in search frame 
        self.logo=Label(search_frame,image=self.photo_logo2)  
        self.logo.place(x=900,y=0,width=50,height=30)      
        
        #Preview or output screen
        #Table Frame
        table_frame=Frame(down_frame,bd=3,relief=RAISED)
        table_frame.place(x=0,y=60,width=1310,height=110) 
        
        #ADDING SCROLL BAR
        scroll_x=ttk.Scrollbar(table_frame,orient=HORIZONTAL)
        scroll_y=ttk.Scrollbar(table_frame,orient=VERTICAL)
        
        #CREATION OF COLUMNS IN TABLE
        self.employee_table=ttk.Treeview(table_frame,columns=('dep','name','degi','email','address','marriage','dob','doj','idproofcomb','idproof','gender','phone','country','salary'),xscrollcommand=scroll_x.set,yscrollcommand=scroll_y.set)
        
        #Placing of SCROLL BAR IN AXIS 
        scroll_x.pack(side=BOTTOM,fill=X)
        scroll_y.pack(side=RIGHT,fill=Y)
        
        scroll_x.config(command=self.employee_table.xview)
        scroll_y.config(command=self.employee_table.yview)
        
        #ADDING THE REAL NAME INSTEAD OF ALIAS NAME IN TREE VIEW
        self.employee_table.heading("dep",text='Department')
        self.employee_table.heading('name',text='NAME')
        self.employee_table.heading('degi',text='Desgination')
        self.employee_table.heading('email',text='Email')
        self.employee_table.heading('address',text='Address')
        self.employee_table.heading('marriage',text='Marriage Status')
        self.employee_table.heading('dob',text='DOB')
        self.employee_table.heading('doj',text='DOJ')
        self.employee_table.heading('idproofcomb',text='ID Type')
        self.employee_table.heading('idproof',text='ID Proof')
        self.employee_table.heading('gender',text='Gender')
        self.employee_table.heading('phone',text='Phone')
        self.employee_table.heading('country',text='Country')
        self.employee_table.heading('salary',text='Salary')
        
        self.employee_table['show']='headings'
        
        #ADJUSTING THE COLUMN SIZE IN TREE VIEW / UPPAR WALA JO JAGHA THA NA USSKO KAAM KAR RAHE HAI
        self.employee_table.column('dep',width=100)
        self.employee_table.column('name',width=100)
        self.employee_table.column('degi',width=100)
        self.employee_table.column('email',width=100)
        self.employee_table.column('address',width=100)
        self.employee_table.column('marriage',width=100)
        self.employee_table.column('dob',width=100)
        self.employee_table.column('doj',width=100)
        self.employee_table.column('idproofcomb',width=100)
        self.employee_table.column('idproof',width=100)
        self.employee_table.column('gender',width=100)
        self.employee_table.column('phone',width=100)
        self.employee_table.column('country',width=100)
        self.employee_table.column('salary',width=100)
        
        
        
        #PACKING OF COLUMNS IN TREE VIEW
        self.employee_table.pack(fill=BOTH,expand=1)
        self.fetch_data()
        self.employee_table.bind("<ButtonRelease>",self.get_cursor)
   
if __name__=="__main__":
    root=Tk()
    obj=Employee(root)
    root.mainloop()
        
