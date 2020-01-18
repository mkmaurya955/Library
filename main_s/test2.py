from tkinter import *
import pymysql as ms
from tkinter import messagebox
from reverse import *

# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase = "library"

con = ms.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()
lst1=[]
lst2=[]
lst3=[]

def issue():
    global lst3, lst2, lst1

    bid = en2.get()
    sid = en3.get()
    sname = en4.get()
    cl = en5.get()
    issuedfrom = en6.get()
    issuedto = en7.get()
    query='select Book_Id from book'
    try:
        cur.execute(query)
        for i in cur:
            lst1.append(i[0])
        a = int(bid)
        b = int(sid)
        c=type(a)
        d=type(b)

        if c == int and d == int:
            if a in lst1:
                cur.execute("select status from book where Book_Id =" + bid + "")
                for i in cur:
                    status = i[0]

                b_issue = "insert into issue values('"+bid+"','"+sid+"','"+sname+"','"+cl+"','"+issuedfrom+"','"+issuedto+"',NULL)"
                update = "update book set status='issued' where Book_Id =" + bid + ""
                print(b_issue)
                print(update)
                if status == 'avail':
                    print(True)
                    cur.execute(b_issue)
                    cur.commit()
                    cur.execute(update)

                    messagebox.showinfo('Success','Book issued successfully')
                else:
                    messagebox.showinfo('Issued', 'Book has been taken by someone else')
            else:
                messagebox.showinfo('Error', 'You have entered wrong Book Id')
        else:
            messagebox.showinfo('Error', 'Book Id and Student Id must be number')
    except:
        print(False)


lst1.clear()


def submit():
    bid1=en8.get()
    sid=en9.get()
    subdate=en10.get()
    try:
        cur.execute('select book_id from issue')
        for i in cur:
            lst2.append(i[0])
        cur.execute('select stu_id from issue')
        for i in cur:
            lst3.append(i[0])
        a=int(bid1)
        b=int(sid)
        c=type(a)
        d=type(b)
        if c==int and d==int:
            if a in lst2:
                if b in lst3:
                    submit="update issue set submition_date="+subdate+" where book_id="+bid1+""
                    cur.execute(submit)
                    con.commit()
                    print(True)
                    avail="update book set status='avail' where Book_Id="+bid1+""
                    cur.execute(avail)
                    con.commit()
                    messagebox.showinfo('Success','Successfully submitted Book')
                    fine()


                else:
                    messagebox.showinfo('Warning','Wrong Student')
            else:
                messagebox.showinfo('Error','You have entered wrong Book Id')
        else:
            messagebox.showinfo('Error','Book Id and Student Id must be number')
    except:
        print(False)

def fine():
    global lst4,lst5,bid1,d,f
    lst4=[]
    lst5=[]
    lastdate="select issued_to from issue where book_id ="+bid1+""
    cur.execute(lastdate)
    for i in cur:
        lst4.append(i[0])
    subdate="select submition_date from issue where book_id ="+bid1+""
    cur.execute(subdate)
    for i in cur:
        lst5.append(i[0])
    d1=reverse(lst4[0])
    d2=reverse(lst5[0])
    for i in d1:
        d3=''
        if i=='-':
            pass
        else:
            d3=d3+i
    for i in d2:
        d4=''
        if i=='-':
            pass
        else:
            d4=d4+i
    days=int(d4)-int(d3)
    fine=days*10
    f=str(fine)
    d=str(days)
    # Late submission
    l1 = Label(f3, text=" " + d + " days late submission. Have to pay fine Of Rs. " + f + "", bd=5, bg='#333645',
               fg='#fff',
               font=('bookman old style', 30, 'bold',))
    l1.place(relx=0.1, rely=0.25)


def issuebooks():
    global en1, en2, en3, en4, en5, en6, en7, en8, en9, en10,f3
    root = Tk()
    root.title("Library")
    root.minsize(width=400, height=400)
    root.geometry("1350x700+0+0")
    title = Label(root, text="Welcome to Sterling's Library", bd=10, relief=GROOVE,
                  font=("algerian", 40, "bold"), bg="violet", fg="black")
    title.pack(side=TOP, fill=X)

    f1 = Frame(root, bg='#333945', bd=10, relief=GROOVE)
    f1.place(relx=0.02, rely=0.15, relwidth=0.45, relheight=0.6)

    f2 = Frame(root, bg='#333945', bd=10, relief=GROOVE)
    f2.place(relx=0.52, rely=0.15, relwidth=0.45, relheight=0.6)

    f3 = Frame(root, bg='#333945', bd=10, relief=GROOVE)
    f3.place(relx=0.02, rely=0.78, relwidth=0.95, relheight=0.2)

    lb1 = Label(f1, text='Issue Book', font=('bookman old style', 24, 'bold'), bd=10, relief=GROOVE)
    lb1.place(relx=0.35, rely=0.01)

    # Book ID

    lb2 = Label(f1, text="Book Id : ", bg='black', fg='white', bd=5, font=("bookman old style", 12, "bold"))
    lb2.place(relx=0.05, rely=0.2)
    en2 = Entry(f1)
    en2.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)
    # Student id

    lb3 = Label(f1, text="Student Id : ", bg='black', fg='white', bd=5, font=("bookman old style", 12, "bold"))
    lb3.place(relx=0.05, rely=0.3)
    en3 = Entry(f1)
    en3.place(relx=0.3, rely=0.3, relwidth=0.62, relheight=0.08)

    # Student name
    lb4 = Label(f1, text="Student name : ", bg='black', fg='white', bd=5, font=("bookman old style", 12, "bold"))
    lb4.place(relx=0.05, rely=0.4)
    en4 = Entry(f1)
    en4.place(relx=0.3, rely=0.4, relwidth=0.62, relheight=0.08)

    # calss
    lb5 = Label(f1, text="Class : ", bg='black', fg='white', bd=5, font=("bookman old style", 12, "bold"))
    lb5.place(relx=0.05, rely=0.5)
    en5 = Entry(f1)
    en5.place(relx=0.3, rely=0.5, relwidth=0.62, relheight=0.08)

    # issued from/to
    lb6 = Label(f1, text='Issued from :', bg='black', fg='white', bd=5, font=("bookman old style", 12, "bold"))
    lb6.place(relx=0.05, rely=0.6)
    en6 = Entry(f1)
    en6.place(relx=0.3, rely=0.6, relwidth=0.25, relheight=0.08)

    lb7 = Label(f1, text='to :', bg='black', fg='white', bd=5, font=("bookman old style", 12, "bold"))
    lb7.place(relx=0.58, rely=0.6)
    en7 = Entry(f1)
    en7.place(relx=0.68, rely=0.6, relwidth=0.25, relheight=0.08)

    # Submit
    btn = Button(f1, text='Issue', bd=10, bg='#f7f1e3', relief=GROOVE, font=("bookman old style", 16, "bold"),
                 command=issue)
    btn.place(relx=0.2, rely=0.8, relwidth=0.25, relheight=0.13)

    lebel2 = Label(f2, text='Submit Book', font=('bookman old style', 24, 'bold'), bd=10, relief=GROOVE)
    lebel2.place(relx=0.30, rely=0.01)

    # Book id

    lb8 = Label(f2, text="Book Id : ", bg='black', fg='white', font=("bookman old style", 14, "bold"))
    lb8.place(relx=0.05, rely=0.2)
    en8 = Entry(f2)
    en8.place(relx=0.3, rely=0.2, relwidth=0.62, relheight=0.08)

    # Student Id
    lb9 = Label(f2, text="Student Id : ", bg='black', fg='white', font=("bookman old style", 14, "bold"))
    lb9.place(relx=0.05, rely=0.4)
    en9 = Entry(f2)
    en9.place(relx=0.3, rely=0.4, relwidth=0.62, relheight=0.08)
    # submiton date

    lb10 = Label(f2, text='Submition Date :', bg='black', fg='white', font=("bookman old style", 14, "bold"))
    lb10.place(relx=0.05, rely=0.6)
    en10 = Entry(f2)
    en10.place(relx=0.4, rely=0.6, relwidth=0.25, relheight=0.08)

    # Submit
    btn = Button(f2, text='Submit', bd=10, bg='#f7f1e3', relief=GROOVE, font=("bookman old style", 16, "bold"),command=submit)
    btn.place(relx=0.2, rely=0.8, relwidth=0.25, relheight=0.13)



    root.mainloop()


issuebooks()
