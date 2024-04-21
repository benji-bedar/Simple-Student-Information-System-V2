import tkinter as tk
from tkinter import Button, StringVar, Widget, ttk
import tkinter.messagebox as tkm
from tkinter.constants import END
import os                       #for file directory
from tkinter import filedialog
from PIL import Image, ImageTk
#import pymysql
import mysql.connector


root = tk.Tk()

root.geometry("1350x700+0+0")
root.title("SSIS Version 2")      
#image_file = r"C:\Users\Amazing User\Pictures\gridbg3.png"
#image_file = r"C:\Users\yuyun\OneDrive\Pictures\Saved Pictures\gridbg3.png"
#image = tk.PhotoImage(file=image_file)

#root.config(background="white")
style = ttk.Style()

title_label = tk.Label(
    root,
    text="SIMPLE STUDENT INFORMATION SYSTEM",
    font=("Times", 20, "bold"),
    padx=15,
    pady=15, 
    border=0, 
    relief=tk.RIDGE, 
    bg="#55a5af",
    foreground="black"
    )
title_label.pack(side=tk.TOP, fill=tk.X)

# Background image
# canvas = tk.Canvas(root, width=image.width(), height=image.height())
# canvas.create_image(0, 0, anchor=tk.NW, image=image)
# canvas.pack()
#Left Menu

detail_frame = tk.LabelFrame(
  root, text="Student Records", 
  font=("Arial", 14),
  border=2, 
  bg="#1a6a74", 
  foreground="black",
  relief=tk.RAISED
)
detail_frame.place(x=40, y=90, width=420, height=570)

# Coure detail Frame
course_detail_frame = tk.LabelFrame(
    root, text="Course Records", 
    font=("Arial", 14),
    border=2, 
    bg="#1a6a74", 
    foreground="black",
    relief=tk.RAISED
    )
course_detail_frame.place(x=40, y=90, width=420, height=570)

#Label with Entry for Course Detail Frame

COURSE_CODE = StringVar()
course_code = tk.Label(course_detail_frame,text="Course Code:", font=("Times", 12), bg="#1a6a74", foreground="black")
course_code.place(x=20, y=20)
cc_entry = tk.Entry(course_detail_frame, textvariable=COURSE_CODE, bd=1,font=("Times", 16),relief=tk.SUNKEN, bg="white", foreground="black")
cc_entry.place(x=130, y=20, width=250, height=30)

COURSE_NAME = StringVar()
courname_label = tk.Label(course_detail_frame,text="Course:", font=("Times", 14), bg="#1a6a74", foreground="black")
courname_label.place(x=20, y=70)
courname_entry = tk.Entry(course_detail_frame, textvariable=COURSE_NAME, bd=1,font=("Times", 16),relief=tk.SUNKEN, bg="white", foreground="black")
courname_entry.place(x=130, y=70, width=250, height=30)

#Label with Entry for Detail Frame

id_label = tk.Label(detail_frame,text="ID No.:", font=("Times", 14), bg="#1a6a74", foreground="black")
id_label.place(x=20, y=20)
ID = StringVar()
id_entry = tk.Entry(detail_frame, textvariable=ID, bd=1,font=("Times", 16),relief=tk.SUNKEN, bg="white", foreground="black")
id_entry.place(x=130, y=20, width=250, height=30)

NAME = StringVar()
name_label = tk.Label(detail_frame,text="Name:", font=("Times", 14), bg="#1a6a74", foreground="black")
name_label.place(x=20, y=70)
name_entry = tk.Entry(detail_frame, textvariable=NAME, bd=1,font=("Times", 16),relief=tk.SUNKEN, bg="white", foreground="black")
name_entry.place(x=130, y=70, width=250, height=30)

GENDER = StringVar()
gender_label = tk.Label(detail_frame,text="Gender:", font=("Times", 14), bg="#1a6a74", foreground="black")
gender_label.place(x=20, y=120)
gender_entry = ttk.Combobox(detail_frame, textvariable=GENDER,font=("Times", 14))
gender_entry["values"] = ("Male", "Female")
gender_entry.place(x=130, y=120, width=250, height=30)

AGE = StringVar()
age_label = tk.Label(detail_frame,text="Age:", font=("Times", 14), bg="#1a6a74", foreground="black")
age_label.place(x=20, y=170)
age_entry = ttk.Spinbox(detail_frame, textvariable=AGE,font=("Times", 14), from_=16, to=130)
age_entry.place(x=130, y=170, width=250, height=30)

COURSE = StringVar()
course_label = tk.Label(detail_frame,text="Course Code:", font=("Times", 13), bg="#1a6a74", foreground="black")
course_label.place(x=20, y=220)
course_entry = tk.Entry(detail_frame, textvariable=COURSE, bd=1,font=("Times", 16),relief=tk.SUNKEN, bg="white", foreground="black")
course_entry.place(x=130, y=220, width=250, height=30)

YEAR = StringVar()
yrlvl_label = tk.Label(detail_frame,text="Year Level:", font=("Times", 14), bg="#1a6a74", foreground="black")
yrlvl_label.place(x=20, y=270)
yrlvl_entry = ttk.Combobox(detail_frame, textvariable=YEAR,font=("Times", 14))
yrlvl_entry["values"] = ("1st Year", "2nd Year", "3rd Year", "4rth Year")
yrlvl_entry.place(x=130, y=270, width=250, height=30)

EMAIL = StringVar()
email_label = tk.Label(detail_frame,text="Email:", font=("Times", 14), bg="#1a6a74", foreground="black")
email_label.place(x=20, y=320)
email_entry = tk.Entry(detail_frame, textvariable=EMAIL, bd=1,font=("Times", 16),relief=tk.SUNKEN, bg="white", foreground="black")
email_entry.place(x=130, y=320, width=250, height=30)


# Single Database frame - Frame for Editing Student

subdata_frame = tk.Frame(
  root,  
  bg="#55a5af",
  relief=tk.GROOVE
)
subdata_frame.place(x=490, y=130, width=830, height=530)

subtitle_label = tk.Label(
    subdata_frame,
    text="Student Details",
    font=("Times", 14, "bold"),
    padx=8,
    pady=8, 
    border=0, 
    relief=tk.RIDGE, 
    bg="#55a5af",
    foreground="white"
    )
subtitle_label.pack(side=tk.TOP, fill=tk.X)

# Single Data Labels and Entries
tk.Label(subdata_frame,text="ID Number: ", font=("Times", 14, "bold"), bg="#55a5af", foreground="black").place(x=30, y=60)
tk.Label(subdata_frame,text="FULL NAME: ", font=("Times", 14, "bold"), bg="#55a5af", foreground="black").place(x=30, y=110)
tk.Label(subdata_frame,text="GENDER: ", font=("Times", 14, "bold"), bg="#55a5af", foreground="black").place(x=30, y=160)
tk.Label(subdata_frame,text="AGE: ", font=("Times", 14, "bold"), bg="#55a5af", foreground="black").place(x=30, y=210)
tk.Label(subdata_frame,text="COURSE CODE: ", font=("Times", 14, "bold"), bg="#55a5af", foreground="black").place(x=30, y=260)
tk.Label(subdata_frame,text="YEAR LEVEL: ", font=("Times", 14, "bold"), bg="#55a5af", foreground="black").place(x=30, y=310)
tk.Label(subdata_frame,text="EMAIL:", font=("Times", 14, "bold"), bg="#55a5af", foreground="black").place(x=30, y=360)


id1_entry = tk.Entry(subdata_frame, bd=1,font=("Times", 14), bg="white", foreground="black")
id1_entry.place(x=230, y=60, width=300, height=28)
name1_entry = tk.Entry(subdata_frame, bd=1,font=("Times", 14), bg="white", foreground="black")
name1_entry.place(x=230, y=110, width=300, height=28)
gender1_entry = ttk.Combobox(subdata_frame, font=("Times", 14))
gender1_entry["values"] = ("Male", "Female")
gender1_entry.place(x=230, y=160, width=300, height=28)
age1_entry = tk.Entry(subdata_frame, bd=1,font=("Times", 14), bg="white", foreground="black")
age1_entry.place(x=230, y=210, width=300, height=28)
courcode_entry = tk.Entry(subdata_frame, bd=1,font=("Times", 14), bg="white", foreground="black")
courcode_entry.place(x=230, y=260, width=300, height=28)

year1_entry = ttk.Combobox(subdata_frame,font=("Times", 14))
year1_entry["values"] = ("1st Year", "2nd Year", "3rd Year", "4rth Year")
year1_entry.place(x=230, y=310, width=300, height=28)
email1_entry = tk.Entry(subdata_frame, bd=1,font=("Times", 14), bg="white", foreground="black")
email1_entry.place(x=230, y=360, width=300, height=28)


#f = tk.Frame(subdata_frame, bd=3, bg="blue", width=230, height=230, relief="groove")
#f.place(x=565, y=60)

#pp_file = r"C:\Users\benji\OneDrive\Desktop\My projects\SSIS\hans\profile.png"
#image = Image.open(pp_file)
#pp = ImageTk.PhotoImage(image)

#lbl = tk.Label(f, bg="black", image=pp)
#lbl.place(x=0, y=0)

# DATA FRAMES

# Third Data Frame
# Frame for student list
data_frame = tk.Frame(
  root,  
  bg="black",
  relief=tk.GROOVE
)
data_frame.place(x=490, y=130, width=830, height=530)

# Frame for course list
sub1data_frame = tk.Frame(
  root,  
  bg="black",
  relief=tk.GROOVE
)
sub1data_frame.place(x=490, y=130, width=830, height=530)

#Database frame 

# Frame for Student Data
main_frame = tk.Frame(
  data_frame,
  bg="black",
  bd=2,
  relief=tk.GROOVE
)
main_frame.pack(fill=tk.BOTH, expand=True)

y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

# Frame for Course Data
submain_frame = tk.Frame(
  sub1data_frame,
  bg="black",
  bd=2,
  relief=tk.GROOVE
)
submain_frame.pack(fill=tk.BOTH, expand=True)

y1_scroll = tk.Scrollbar(submain_frame, orient=tk.VERTICAL)
x1_scroll = tk.Scrollbar(submain_frame, orient=tk.HORIZONTAL)


#Treeview database

# Student Table
student_table = ttk.Treeview(main_frame, columns=(
  "ID", "Name", "Gender", "Year Level","Age", "Email", "Course Code"
), yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

y_scroll.config(command=student_table.yview)
x_scroll.config(command=student_table.xview)

y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

student_table.heading("ID", text="ID No.")
student_table.heading("Name", text="Name")
student_table.heading("Gender", text="Gender")
student_table.heading("Year Level", text="Year Level")
student_table.heading("Age", text="Age")
student_table.heading("Email", text="Email")
student_table.heading("Course Code", text="Course Code")

student_table["show"] = "headings"

student_table.column("ID", width=100)
student_table.column("Name", width=100)
student_table.column("Gender", width=100)
student_table.column("Year Level", width=100)
student_table.column("Age", width=100)
student_table.column("Email", width=100)
student_table.column("Course Code", width=100)


student_table.pack(fill=tk.BOTH, expand=True)

# Course Table
course_table = ttk.Treeview(submain_frame, columns=(
  "Course Code", "Course"
), yscrollcommand=y1_scroll.set, xscrollcommand=x1_scroll.set)

y1_scroll.config(command=course_table.yview)
x1_scroll.config(command=course_table.xview)

y1_scroll.pack(side=tk.RIGHT, fill=tk.Y)
x1_scroll.pack(side=tk.BOTTOM, fill=tk.X)

course_table.heading("Course Code", text="Course Code")
course_table.heading("Course", text="Course")

course_table["show"] = "headings"

course_table.column("Course Code", width=100)
course_table.column("Course", width=100)

course_table.pack(fill=tk.BOTH, expand=True)

global button_frame
# FUNCTIONS

class Student:
    def add():
        try:
                
            id = id_entry.get()
            n1 = name_entry.get() 
            g1 = gender_entry.get() 
            c1 = course_entry.get() 
            y1 = yrlvl_entry.get() 
            a1 = age_entry.get() 
            e1 = email_entry.get()
            if id =='' or n1 =='' or g1 =='' or c1 =='' or y1 =='' or a1 =='' or e1=='': 
                tkm.showinfo("SSIS Messsage!", "Fill-in missing details!")
                return
            else:
                conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='ssisv2'

            )
                cursor = conn.cursor()
                table_create_query = '''CREATE TABLE IF NOT EXISTS 
                                    Student_Data(id_num INT, stud_name TEXT, gender TEXT, course TEXT, 
                                    year_lvl TEXT, age INT, email TEXT, PRIMARY KEY (id_num))'''  
                cursor.execute(table_create_query)
            
            # Insert Data
                data_insert_query = '''INSERT INTO Student_Data(id_num, stud_name, gender, course, 
                                    year_lvl, age, email) VALUES (%s, %s, %s, %s, %s, %s, %s)'''
                data_insert_tuple = (id,n1,g1,c1,y1,a1,e1)

                cursor.execute(data_insert_query, data_insert_tuple)
                conn.commit()

                Student.refresh_frame()
                Student.clearAll()
                tkm.showinfo("SSIS Messsage!", "Data saved successfully!")
                conn.close()
        except:
            tkm.showinfo("SSIS Messsage!", "Data already exists!")
            Student.refresh_frame()

    def edit(event=None):
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ssisv2'
        )        

        #back_btn2.destroy()

        cursor = conn.cursor()

        #search_btn.config(state="disable")
        item = student_table.focus() or course_table.focus()    
        values = student_table.item(item)['values'] or course_table.item(item)['values']
        cc = values[3]

        cursor.execute("SELECT course FROM Course_Data WHERE course_code = %s", (cc,))
        course = cursor.fetchone()
        course = (course[0] if course else "")

        subdata_frame.lift()

        id1_entry.insert(0, values[0])
        name1_entry.insert(0, values[1])
        gender1_entry.insert(0, values[2])
        age1_entry.insert(0, values[4])
        courcode_entry.insert(0,values[6])
        #course1_entry.insert(0, course if course else "")        
        year1_entry.insert(0, values[3])
        email1_entry.insert(0, values[5])
        

        #img = (Image.open("SSIS ProPic/"+ str(id1_entry.get()) + ".jpg"))
        #resized = img.resize((220,220))
        #photo = ImageTk.PhotoImage(resized)
        #lbl.config(image=photo)
        #lbl.image = photo

        conn.close()
        Student.clearAll()

    def save():
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ssisv2'
        )
        cursor = conn.cursor()
        item = student_table.focus()
        init_id = student_table.item(item)['values'][0]

        id = id1_entry.get()
        n1 = name1_entry.get() 
        gn1 = gender1_entry.get() 
        a1 = age1_entry.get() 
        c1 =courcode_entry.get() 
        #c2 = course1_entry.get()
        yr1 = year1_entry.get() 
        e1 = email1_entry.get()
        if id =='' or n1 =='' or gn1 =='' or c1 =='' or yr1 =='' or a1 =='' or e1=='':
            tkm.showinfo("SSIS Messsage!", "Fill-in missing details!")
            return
        else:
          
          # Update Data
          data_update_query = '''UPDATE Student_Data SET id_num = %s, stud_name = %s, gender = %s, course = %s, 
                                year_lvl = %s, age = %s, email = %s WHERE id_num = %s'''
          data_update_tuple = (id,n1,gn1,c1,yr1,a1,e1,init_id)
          
          cursor.execute(data_update_query, data_update_tuple)
          conn.commit()

        #try:
        #    img.save("SSIS ProPic/"+ str(id1_entry.get() + ".jpg"))          
        #except:
        #  tkm.showinfo("SSIS Messsage!", "No Image Selected!")

        tkm.showinfo("SSIS Message!", "Data updated successfully!")
        conn.close()

    def delete():
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ssisv2'
        )        
        cursor = conn.cursor()

        item = student_table.focus() or course_table.focus()
        id_num = student_table.item(item)['values'][0] or course_table.item(item)['values'][0]
        cursor.execute("SELECT * FROM Student_Data WHERE id_num = %s", (id_num,))
        data = cursor.fetchall()

        if data is not None:
        # Delete the row from the database
            result = tkm.askyesno("Quit", "Are you sure you want to delete?")
            if result == tk.YES:
                cursor.execute("DELETE FROM Student_Data WHERE id_num = %s", (id_num,))
                conn.commit()
                Student.refresh_frame()     
                data_frame.lift()
                tkm.showinfo("SSIS Message!", "Data deleted successfully!")
            else:
                return                        

        cursor.close()
        conn.close()
        
    def clearAll():
        ID.set('')
        NAME.set('')
        GENDER.set('')
        COURSE.set('')
        YEAR.set('')
        AGE.set('')
        EMAIL.set('')

    def search(event=None):
        global back_btn2
        global count
        count = 0
        data_frame.lift()
        def back1():
            Student.refresh_frame()
            back_btn2.destroy()
            return

        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ssisv2'
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Student_Data")
        data = cursor.fetchall()
        index = 0
        search_query = search_entry.get().lower()
        # Clear the data_frame
        if search_query == '':
            index +=1
            count += 1
            Student.refresh_frame()
        else:
            student_table.delete(*student_table.get_children())
        
            # Search for matching students by name or ID
            for student in data:   
                if search_query in student[1].lower() or search_query == str(student[0]):
                    # Insert the matching student into the data_frame
                    student_table.insert('', 'end', values=(student[0], student[1], student[2], student[3], student[4], student[5], student[6]))
                    index +=1
            back_btn2 = tk.Button(data_frame, bg="black",foreground="white", text=" BACK ", compound="right", relief=tk.RAISED, bd=2,font=("Times", 12), width=15, command=back1)
            back_btn2.place(x=320, y=480, width=175, height=29)

        if index == 0:
            tkm.showinfo("SSIS Messsage!", "No student found!")
            #back1()
            Student.refresh_frame()
        
        conn.close()

    def refresh_frame():
        conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='',
            database='ssisv2'
        )
        cursor = conn.cursor()

        # Clear existing data
        student_table.delete(*student_table.get_children())
        course_table.delete(*course_table.get_children())

        # Fetch data from the database
        cursor.execute('SELECT * FROM Student_Data')        
        rows = cursor.fetchall()
        student_table.tag_configure("oddrow", background="white")
        student_table.tag_configure("evenrow", background="lightgrey", foreground="black")
        course_table.tag_configure("oddrow", background="white")
        course_table.tag_configure("evenrow", background="lightgrey", foreground="black")

        count = 0
        # Insert fetched data into the treeview
        for row in rows:
            #student_table.insert('', tk.END, values=row)  <-- No Stripes

            if count % 2 == 0:
                student_table.insert(parent="", index="end", iid=count, text="", values=row, tags=("evenrow"))
            else:
                student_table.insert(parent="", index="end", iid=count, text="", values=row, tags=("oddrow"))
            count += 1        

        count1 = 0
        cursor1 = conn.cursor()
        cursor1.execute("SELECT * FROM Course_Data")
        rows1 = cursor1.fetchall()
        for row1 in rows1:
            #student_table.insert('', tk.END, values=row)  <-- No Stripes

            if count1 % 2 == 0:
                course_table.insert(parent="", index="end", iid=count1, text="", values=row1, tags=("evenrow"))
            else:
                course_table.insert(parent="", index="end", iid=count1, text="", values=row1, tags=("oddrow"))
            count1 += 1  

        search_entry.delete(0, tk.END)
        conn.close()
        
    def showImage():
        global filename
        global img
        filename = filedialog.askopenfilename(initialdir =os.getcwd(),title="Selec image file", filetype=(("JPG File", "*.jpg"),("PNG File", "*.png"),("All files", "*.txt")))
        if filename:  
          img = (Image.open(filename))
          resized = img.resize((220,220))
          photo = ImageTk.PhotoImage(resized)
          #lbl.config(image=photo)
          #lbl.image = photo

    def exit():
        student_table.selection_remove(student_table.focus())
        course_table.selection_remove(course_table.focus())
        result = tkm.askyesno("Quit", "Are you sure you want to quit?")
        if result == tk.YES:
            root.quit()  # Quit the Tkinter application
        else:
            return

    def back():
        student_table.selection_remove(student_table.focus())
        course_table.selection_remove(course_table.focus())
        search_btn.config(state="normal")
        id1_entry.delete(0, "end")
        name1_entry.delete(0, "end")
        gender1_entry.delete(0, "end")
        age1_entry.delete(0, "end")
        #course1_entry.delete(0, "end")
        courcode_entry.delete(0, "end")
        year1_entry.delete(0, "end")
        email1_entry.delete(0, "end")

        #lbl.config(image=pp)
        #lbl.image = pp
        Student.refresh_frame()        
        data_frame.lift()

    def on_focus_in(event):
        text = event.widget
        if text.get() == 'Enter ID no. or Name...':
                text.delete(0, 'end')
                text.configure(foreground='black')

    def on_focus_out(event):
        text = event.widget
        if text.get() == '':
            text.insert(0, 'Enter ID no. or Name...')
            text.configure(foreground='grey')
            #text.config(show='Enter ID no. or Name')

    # Functions for Course Detail Frame
    def add_course():
        try:
            cc = cc_entry.get()
            cname = courname_entry.get()
            if cc =='' or cname=='': 
                tkm.showinfo("SSIS Messsage!", "Fill-in missing details!")
                return
            else:
                conn = mysql.connector.connect(
                host='localhost',
                user='root',
                password='',
                database='ssisv2'
            )   
                cursor = conn.cursor()
                table_create_query = '''CREATE TABLE IF NOT EXISTS 
                                    Course_Data(course_code VARCHAR(20), course TEXT, PRIMARY KEY (course_code))'''  
                cursor.execute(table_create_query)

                course_insert_query = '''INSERT INTO Course_Data(course_code, course) VALUES (%s, %s)'''
                course_insert_tuple = (cc,cname)

                cursor.execute(course_insert_query, course_insert_tuple)
                conn.commit()

                Student.refresh_frame()
                COURSE_CODE.set('')
                COURSE_NAME.set('')
                tkm.showinfo("SSIS Messsage!", "Data saved successfully!")
                conn.close()
        except:
            tkm.showinfo("SSIS Messsage!", "Data already exists!")
            COURSE_CODE.set('')
            COURSE_NAME.set('')            

    def edit_course(event=None):
        COURSE_CODE.set('')
        COURSE_NAME.set('')
        item = course_table.focus()
        values = course_table.item(item)['values']

        cc_entry.insert(0, values[0])
        courname_entry.insert(0, values[1])

    def save_course():
    
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ssisv2'
        )
        cursor = conn.cursor()
        item = course_table.focus()
        init_code = course_table.item(item)['values'][0]


        cc = cc_entry.get()
        cname = courname_entry.get() 

        if cc =='' or cname=='':
            tkm.showinfo("SSIS Messsage!", "Fill-in missing details!")
            return
        else:
        
        # Update Data
            data_update_query = '''UPDATE Student_Data SET course = %s WHERE course = %s'''
            data_update_tuple = (cc,init_code)

            course_update_query = '''UPDATE Course_Data SET course_code = %s, course = %s WHERE course_code = %s'''
            course_update_tuple = (cc,cname,init_code)
            
            cursor.execute(data_update_query, data_update_tuple)
            cursor.execute(course_update_query, course_update_tuple)
            tkm.showinfo("SSIS Messsage!", "Data saved successfully!")          
            conn.commit()
        Student.refresh_frame()
        COURSE_CODE.set('')
        COURSE_NAME.set('')
        
        
    def delete_course():
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ssisv2'
        )        
        cursor = conn.cursor()
        item = course_table.focus()
        values = course_table.item(item)['values']
        cc = values[0]
        cursor.execute("SELECT * FROM Course_Data WHERE course_code = %s", (cc,))
        data = cursor.fetchall()

        if data is not None:
        # Delete the row from the database
            result = tkm.askyesno("Quit", "Are you sure you want to delete?")
            if result == tk.YES:
                cursor.execute("DELETE FROM Course_Data WHERE course_code = %s", (cc,))
                delete_student_course_query = '''UPDATE Student_data SET course = NULL WHERE course = %s'''
                cursor.execute(delete_student_course_query, (cc,))

                conn.commit()
                Student.refresh_frame()     
                tkm.showinfo("SSIS Message!", "Data deleted successfully!")
            else:
                return                        

        cursor.close()
        conn.close()

    def mngStudent():
        detail_frame.lift()
        data_frame.lift()

    def mngCourse():
        course_detail_frame.lift()
        sub1data_frame.lift()            
    

student_table.selection_remove(student_table.focus())
course_table.selection_remove(course_table.focus())
conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='ssisv2'
        )

student_table.tag_configure("oddrow", background="white")
student_table.tag_configure("evenrow", background="lightgrey")
course_table.tag_configure("oddrow", background="white")
course_table.tag_configure("evenrow", background="lightgrey")

# Fill course table
cursor1 = conn.cursor()
cursor1.execute("SELECT * FROM Course_Data")
data1 = cursor1.fetchall()

count1 = 0
for record in data1:
    if count1 % 2 == 0:
        course_table.insert(parent="", index="end", iid=count1, text="", values=record, tags=("evenrow"))
    else:
        course_table.insert(parent="", index="end", iid=count1, text="", values=record, tags=("oddrow"))
    count1 += 1

# Fill student table
cursor = conn.cursor()
cursor.execute("SELECT * FROM Student_Data")
data = cursor.fetchall()

count = 0
for record in data:
    if count % 2 == 0:
        student_table.insert(parent="", index="end", iid=count, text="", values=record, tags=("evenrow"))
    else:
        student_table.insert(parent="", index="end", iid=count, text="", values=record, tags=("oddrow"))
    count += 1

# Close the database connection
conn.close()


# BUTTONS

button_frame = tk.Frame(detail_frame, bg="#1a6a74",bd=0, relief= tk.GROOVE)    
button_frame.place(x=40, y=400, width=332, height=90)

add_btn = tk.Button(button_frame,bg="black",foreground="white",text="ADD",bd=2,font=("Times", 13), width=8, command=Student.add)
add_btn.grid(row=0, column=0, padx=2, pady=2)

edit_btn = tk.Button(button_frame,bg="black",foreground="white",text="EDIT",bd=2,font=("Times", 13), width=8, command=Student.edit)
edit_btn.grid(row=0, column=1, padx=2, pady=2)
student_table.bind('<Double-Button-1>', Student.edit)

#quit_btn = tk.Button(button_frame,bg="black",foreground="white",text="QUIT",bd=2,font=("Times", 13), width=15,command=Student.exit)
#quit_btn.grid(row=1, column=1, padx=2, pady=2)

delete_btn = tk.Button(button_frame,bg="black",foreground="white",text="DELETE",bd=2,font=("Times", 13), width=8, command=Student.delete)
delete_btn.grid(row=0, column=2, padx=2, pady=2)

course_btn = tk.Button(detail_frame,bg="white",foreground="blue",text="COURSES",bd=2,font=("Times", 15), width=20, command=Student.mngCourse)
course_btn.place(x= 100, y= 500)

# Buttons for Course Detail Frame

course_button_frame = tk.Frame(course_detail_frame, bg="#1a6a74",bd=0, relief= tk.GROOVE)    
course_button_frame.place(x=40, y=350, width=332, height=130)

add_btn = tk.Button(course_button_frame,bg="black",foreground="white",text="ADD",bd=2,font=("Times", 13), width=15, command=Student.add_course)
add_btn.grid(row=0, column=0, padx=2, pady=2)

edit_btn = tk.Button(course_button_frame,bg="black",foreground="white",text="EDIT",bd=2,font=("Times", 13), width=15, command=Student.edit_course)
edit_btn.grid(row=0, column=1, padx=2, pady=2)
course_table.bind('<Double-Button-1>', Student.edit_course)

saveCour_btn = tk.Button(course_button_frame,bg="black",foreground="white",text="SAVE",bd=2,font=("Times", 13), width=15, command=Student.save_course)
saveCour_btn.grid(row=1, column=0, padx=2, pady=2)

delete_btn = tk.Button(course_button_frame,bg="black",foreground="white",text="DELETE",bd=2,font=("Times", 13), width=15, command=Student.delete_course)
delete_btn.grid(row=1, column=1, padx=2, pady=2)

student_btn = tk.Button(course_detail_frame,bg="white",foreground="blue",text="STUDENTS",bd=2,font=("Times", 15), width=20, command=Student.mngStudent)
student_btn.place(x= 100, y= 500)

for button in course_button_frame.winfo_children():
    button.grid_configure(padx=10, pady=5)

#quit_btn = tk.Button(course_button_frame,bg="black",foreground="white",text="QUIT",bd=3,font=("Times", 14), width=15,command=Student.exit)
#quit_btn.place(x=80, y=90, width=160, height=33)

# Subdata Bttn
back_btn = tk.Button(subdata_frame,bg="black",foreground="white",text="BACK",bd=2,font=("Times", 13), width=15, command=Student.back)
back_btn.place(x=450, y=460)

#upload_btn = tk.Button(subdata_frame,bg="black",foreground="white",text="UPLOAD",bd=2,font=("Times", 13), width=15, command=Student.showImage)
#upload_btn.place(x=600, y=300)
#f = tk.Frame(subdata_frame, bd=3, bg="blue", width=230, height=230, relief="groove")
#f.place(x=565, y=60)

save1_btn = tk.Button(subdata_frame,bg="black",foreground="white",text="SAVE",bd=2,font=("Times", 13), width=15, command=Student.save)
save1_btn.place(x = 240, y=460)
#del_btn = tk.Button(subdata_frame,bg="black",foreground="white",text="DELETE",bd=2,font=("Times", 13), width=15, command=Student.delete)
#del_btn.place(x=600, y=200)

for button in button_frame.winfo_children():
    button.grid_configure(padx=10, pady=5)

#search_icon = r"C:\Users\Amazing User\Pictures\search_icon.png"
search_icon = r"C:\Users\benji\OneDrive\Desktop\My projects\SSIS\hans\button.png"
search_logo = tk.PhotoImage(file=search_icon)
root.bind('<Return>', Student.search)
search_btn = tk.Button(root, bg="black", compound="right", image=search_logo, relief=tk.RAISED, bd=2, width=15, command=Student.search)
search_btn.place(x=490, y=90, width=60, height=30)

search_entry = tk.Entry(root, bd=3,font=("Times", 14),relief=tk.SUNKEN, bg="white", foreground="white")
search_entry.insert(0, 'Enter ID no. or Name...')
search_entry.configure(foreground='grey')
search_entry.bind('<FocusIn>', Student.on_focus_in)
search_entry.bind('<FocusOut>', Student.on_focus_out)
search_entry.place(x=555, y=90, width=250, height=29)

courList_btn = tk.Button(root, bg="gray",foreground="blue", text="COURSE LIST", relief=tk.RAISED, bd=2,font=("Times", 12), width=15, command=sub1data_frame.lift)
courList_btn.place(x=980, y=90, width=150, height=28)

studList_btn = tk.Button(root, bg="gray",foreground="blue", text="STUDENT LIST", relief=tk.RAISED, bd=2,font=("Times", 12), width=15, command=data_frame.lift)
studList_btn.place(x=1150, y=90, width=150, height=28)


root.mainloop()
 