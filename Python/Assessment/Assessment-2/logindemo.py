from tkinter import *
from tkinter import ttk
import mysql.connector
from mysql.connector import Error
import tkinter.messagebox as msg

#Define the on_select function combobox
#def on_select(event):
#selected_city = combo_box.get()
#print(f"Selected city: {selected_city}")

#-------------------Create Connection----------------
def create_conn():
    return mysql.connector.connect(
        host="127.0.0.1",
        username="root",
        password="qwertyuiop",
        database="registration"
        )
print (create_conn())

def insert_data():
    print("Insert clicked")
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="":
        msg.showinfo("insertdata","All Fields Requiered")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query = "insert into registrationform(fname, lname, email, mobile, gender, city) values(%s, %s, %s, %s, %s, %s)"
        args = (e_fname.get(), e_lname.get(), e_email.get(), e_mobile.get(), v.get(), combo_box.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        v.set(0)
        combo_box.set('')
        msg.showinfo("Insert status","inserted successfully")

def search_data():
    print("Search clicked")
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')
    v.set(0)
    combo_box.set('')
    if e_id.get()=="":
        msg.showinfo("search status","id mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="select * from registrationform where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        row=cursor.fetchall()
        if row:
            e_fname.insert(0,row[0][1])
            e_lname.insert(0,row[0][2])
            e_email.insert(0,row[0][3])
            e_mobile.insert(0,row[0][4])
            v.set(0,row[0][5])
            combo_box.set(0,row[0][6])
        else:
            msg.showinfo("search status","id not found")
            conn.close()
            
def update_data():
    if e_fname.get()=="" or e_lname.get()=="" or e_email.get()=="" or e_mobile.get()=="" or e_id.get()=="":
        msg.showinfo("insertdata","All Fields Requiered")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="update registrationform set fname=%s,lname=%s,email=%s,mobile=%s,v=%s,combo_box=%s where id=%s"
        args=(e_fname.get(),e_lname.get(),e_email.get(),e_mobile.get(),e_id.get(),v.get(),combo_box.get())
        cursor.execute(query,args)
        conn.commit()
        conn.close()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("update status","data updated successfully")
        
        
def delete_data():
    if e_id.get()=="":
        msg.showinfo("Delete Status","Id Is Mandatory")
    else:
        conn=create_conn()
        cursor=conn.cursor()
        query="delete from registrationform where id=%s"
        args=(e_id.get(),)
        cursor.execute(query,args)
        conn.commit()
        e_fname.delete(0,'end')
        e_lname.delete(0,'end')
        e_email.delete(0,'end')
        e_mobile.delete(0,'end')
        msg.showinfo("Delete Status","Data Deleted Successfully")
        conn.close()
        
def clear_data():
    e_id.delete(0,'end')
    e_fname.delete(0,'end')
    e_lname.delete(0,'end')
    e_email.delete(0,'end')
    e_mobile.delete(0,'end')
    msg.showinfo("clear status","data clear successfully")




root = Tk()
root.geometry("750x500")
root.title("Registration Form")

l_id = Label(root, text="ID")
l_id.place(x=50, y=50)
l_fname = Label(root, text="Fname")
l_fname.place(x=50, y=100)
l_lname = Label(root, text="Lname")
l_lname.place(x=50, y=150)
l_email = Label(root, text="Email")
l_email.place(x=50, y=200)
l_mobile = Label(root, text="Mobile")
l_mobile.place(x=50, y=250)
l_gender = Label(root, text="Gender")
l_gender.place(x=50, y=300)

v = IntVar()
Radiobutton(root, text='Male', variable=v, value=1).place(x=150, y=300)
Radiobutton(root, text='Female', variable=v, value=2).place(x=200, y=300)

# Correct the Label and Combobox usage
l_city= Label(root, text="City Name: ")
l_city.place(x=50, y=350)

combo_box = ttk.Combobox(root, values=["Ahmedabad", "Mumbai", "Rajkot"])
combo_box.place(x=150, y=350)

# Bind event to selection
#combo_box.bind("<<ComboboxSelected>>", on_select)

e_id=Entry(root)
e_id.place(x=150,y=50)

e_fname=Entry(root)
e_fname.place(x=150,y=100)

e_lname=Entry(root)
e_lname.place(x=150,y=150)

e_email=Entry(root)
e_email.place(x=150,y=200)

e_mobile=Entry(root)
e_mobile.place(x=150,y=250)

#----------------------------
insert=Button(root,text="Insert",bg="black",fg="white",font=("Times",12),command=insert_data)
insert.place(x=50,y=400)

search=Button(root,text="search",bg="black",fg="white",font=("Times",12),command=search_data)
search.place(x=100,y=400)

update=Button(root,text="Update",bg="black",fg="white",font=("Times",12),command=update_data)
update.place(x=150,y=400)

delete=Button(root,text="Delete",bg="black",fg="white",font=("Times",12),command=delete_data)
delete.place(x=200,y=400)

clear=Button(root,text="Clear",bg="black",fg="white",font=("Times",12),command=clear_data)
clear.place(x=250,y=400)






root.mainloop()
