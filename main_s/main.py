from SearchBook import *
from menu import *


# Add your own database name and password here to reflect in the code
mypass = "root"
mydatabase = "library"

con = ms.connect(host="localhost", user="root", password=mypass, database=mydatabase)
cur = con.cursor()




root = Tk()
root.title("Library")
root.minsize(width=400, height=400)
root.geometry("1350x700+0+0")
title=Label(root, text="Welcome to Sterling's Library", bd=10, relief=GROOVE,
                      font=("algerian", 40, "bold"), bg="violet", fg="black")
title.pack(side=TOP, fill=X)






'''
MAIN PAGE
'''
'''
checking login
'''


def gettingLoginDetails():
    global login, password,getpassword

    login = int(en1.get())
    password = en2.get()

    sqlLoginID = "select login_Id from login where password = '" + password + "'"
    sqlpassword = "select password from login where password = '" + password + "'"

    try:
        cur.execute(sqlLoginID)
        for i in cur:
            getLoginID = i[0]

        cur.execute(sqlpassword)
        for i in cur:
            getpassword = i[0]

        if (getLoginID == login and getpassword == password):
            messagebox.showinfo("SUCCESS", "Login successful, Welcome to MENU Page")
            empMenu()

        else:
            messagebox.showerror("Failure", "Can't log in, check your credentials")
    except:
        messagebox.showinfo("FAILED", "Please check your credentials")


    print(login)
    print(password)



labelFrame = Frame(root,bd=6 ,bg='crimson', relief=RIDGE)
labelFrame.place(relx=0.1, rely=0.2, relwidth=0.8, relheight=0.5)

title=Label(labelFrame, text='Librarian Login',bg ='crimson', fg='white', font=('bookman old style',30,'bold','italic'))
title.place(relx=0.35, rely=0.05)

# Login ID

lb1 = Label(labelFrame, text="Login ID : ", bg='crimson', fg='white',font=('bookman old style',20,'bold'))
lb1.place(relx=0.15, rely=0.30)

en1 = Entry(labelFrame)
en1.place(relx=0.30, rely=0.33, relwidth=0.50,relheight=0.060)

# Password
lb2 = Label(labelFrame, text="Password : ", bg='crimson', fg='white',font=('bookman old style',20,'bold'))
lb2.place(relx=0.15, rely=0.55)

en2 = Entry(labelFrame)
en2.place(relx=0.30, rely=0.57, relwidth=0.50,relheight=0.060)

# Submit Button
SubmitBtn = Button(labelFrame, text="LOGIN", bg='#d1ccc0', fg='black', font=('times new roman',18,'bold'),command=gettingLoginDetails)
SubmitBtn.place(relx=0.30, rely=0.80, relwidth=0.18, relheight=0.08)

# search
labelFrame = Frame(root,bd=6 ,bg='crimson', relief=RIDGE)
labelFrame.place(relx=0.1, rely=0.8, relwidth=0.8, relheight=0.15)

search=Label(labelFrame, text='To see the available book',bg ='crimson', fg='white', font=('bookman old style',20,'bold',))
search.place(relx=0.2, rely=0.3)

click = Button(labelFrame, text="Click Here", bg='#d1ccc0', fg='black', font=('times new roman',18,'bold'), command=View)
click.place(relx=0.6, rely=0.3, relwidth=0.18, relheight=0.4)

root.mainloop()



