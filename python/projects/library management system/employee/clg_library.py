import pymysql
def make_connection():
        conn=pymysql.connect(host="localhost",user="root",password="jjaaiinn1998",database='library')
        cursor=conn.cursor()
        return conn,cursor

def close_connection(conn):
        conn.commit()
        conn.close()
def search_employee(e_id):
    conn,e_cursor = make_connection()
    sql = f"select * from employee_details;"
    e_cursor.execute(sql)
    data = e_cursor.fetchall()
    f = 0
    for employee in data:
        if employee[0] == e_id:
            f=1
            close_connection(conn)
            return True
    if f == 0:
        close_connection(conn)
        return False

def search_student(s_roll):
    conn,e_cursor = make_connection()
    sql = f"select * from student_details;"
    e_cursor.execute(sql)
    data = e_cursor.fetchall()
    f = 0
    for student in data:
        if student[0] == s_roll:
            f=1
            close_connection(conn)
            return True
    if f == 0:
        close_connection(conn)
        return False


def add_book_details():
    bid=input("Enter the book id: ")
    title=input("Enter the title of the book: ")
    subject=input("Enter the subject name: ")
    author=input("Enter the name of the author")
    status=input("Enter the status as \n 'I' for issued \n 'A' for available\n")
    if status=='I':
        status="ISSUED"
    elif status=='A':
        status="AVAILABLE"
    else:
        print("INVALID STATUS INFORMATION")
        status=""
    conn,b_cursor=make_connection()
    sql=f"insert into book values('{bid}','{title}','{subject}','{author}','{status}');"
    b_cursor.execute(sql)
    close_connection(conn)
    print("BOOK ADDED SUCCESFULLY")

def delete_book():
    bid = input("Enter the book id: ")
    conn, b_cursor = make_connection()
    sql = f"select * from book;"
    b_cursor.execute(sql)
    data = b_cursor.fetchall()
    f=0
    for i in data:
        if i[0] == bid:
            f=1
            sql=f"delete from book where bid='{bid}';"
            b_cursor.execute(sql)
            print("BOOK DELETED SUCCESFULLY")
            close_connection(conn)
    if f==0:
        print("BOOK ID IS NOT VALID")
        close_connection(conn)

def view_books():
    conn, b_cursor = make_connection()
    sql = f"select * from book;"
    b_cursor.execute(sql)
    data = b_cursor.fetchall()
    for s_book in data:
        print(s_book[0],s_book[1],s_book[2],s_book[3],s_book[4])
    close_connection(conn)

def search_book():
    title = input("Enter the book title: ")
    conn, b_cursor = make_connection()
    sql = f"select * from book;"
    b_cursor.execute(sql)
    data = b_cursor.fetchall()
    f = 0
    for s_book in data:
        if s_book[1] == title:
            f = 1
            print(s_book[0], s_book[1], s_book[2], s_book[3], s_book[4])
            close_connection(conn)
    if f == 0:
        print("BOOK IS NOT PRESENT IN OUR LIBRARY")
        close_connection(conn)


def issue_book():
    pass
def e_reg():
    conn, e_cursor = make_connection()
    print("ENTER DETAILS")
    e_id=input("ENTER YOUR EMPLOYEE ID: ")
    if search_employee(e_id)==True:
        close_connection(conn)
        print("The employee is already present;")
    else:
        e_name=input("ENTER YOUR NAME: ")
        e_dept=input("ENTER YOUR DEPARTMENT: ")
        e_join_date=input("ENTER YOUR DATE OF JOINING(DD/MM/YYYY): ")
        e_sal=input("ENTER YOUR SALARY")
        e_pass=input("ENTER YOUR PASSWORD: ")
        sql=f"insert into employee_details values('{e_id}','{e_name}','{e_dept}','{e_join_date}','{e_sal}','{e_pass}');"
        e_cursor.execute(sql)
        sql = f"insert into login values('{e_id}','{e_pass}','{e_name}','employee');"
        e_cursor.execute(sql)
        close_connection(conn)
        print("REGESTRATION SUCCESFUL")
def s_reg():
    conn, e_cursor = make_connection()
    print("ENTER DETAILS")
    s_roll=input("ENTER YOUR ROLLNO: ")
    if search_student(s_roll)==True:
        close_connection(conn)
        print("The student is already present")
    else:
        s_name=input("ENTER YOUR NAME: ")
        s_dept=input("ENTER YOUR DEPARTMENT: ")
        s_sem=input("ENTER YOUR SEMESTER: ")
        s_batch=input("ENTER YOUR BATCH")
        s_pass=input("ENTER YOUR PASSWORD: ")
        sql=f"insert into student_details values('{s_roll}','{s_name}','{s_dept}','{s_sem}','{s_batch}','{s_pass}');"
        e_cursor.execute(sql)
        sql = f"insert into login values('{s_roll}','{s_pass}','{s_name}','student');"
        e_cursor.execute(sql)
        close_connection(conn)
        print("REGESTRATION SUCCESFUL")

while True:
    print("Press 1 if u are EMPLOYEE \n Press 2 if you are STUDENT\n")
    op=eval(input("Enter your choice\n"))
    if op==1:
        print("1. LOGIN/SIGNIN \n 2.SIGNUP/REGESTRATION\n")
        ch=eval(input("Enter your choice\n"))
        if ch==1:
           f=0
           conn,mycursor=make_connection()
           l_id=input("Enter your employee id ")
           pwd=input("Enter your password ")
           sql=f"select * from login;"
           mycursor.execute(sql)
           data=mycursor.fetchall()
           for i in data:
               if i[0]==l_id:
                   f=1
                   if i[1]==pwd and i[3]=='employee':
                       print("LOGIN SUCCESFULL")
                       close_connection(conn)
                       print("1.Add book details \n 2.Delete book from record \n 3.View books list \n 4.Search book \n 5. Issue book to student \n")
                       choice=eval(input("Enter your choice \n"))
                       if choice==1:
                           add_book_details()
                       elif choice==2:
                           delete_book()
                       elif choice == 3:
                           view_books()
                       elif choice == 4:
                           search_book()
                       elif choice == 5:
                           issue_book()
                       else:
                           print("INVALID INPUT\n")
                   else:
                       print("INVALID PASSWORD")
                       close_connection(conn)
               if f==0:
                        print("INVALID USERNAME\n")
                        close_connection(conn)
        elif ch==2:
            e_reg()
        else:

            print("INVALID CHOICE")


    elif op==2:
        print("1. LOGIN/SIGNIN \n 2.SIGNUP/REGESTRATION\n")
        ch = eval(input("Enter your choice\n"))
        if ch == 1:
            f = 0
            conn, s_cursor = make_connection()
            s_roll = input("Enter your Roll No.: ")
            pwd=input("Enter your password: ")
            sql = f"select * from login;"
            s_cursor.execute(sql)
            data = s_cursor.fetchall()
            for i in data:
                if i[0] == s_roll:
                    f = 1
                    if i[1] == pwd and i[3]=='student':
                        print("LOGIN SUCCESFULL")
                        close_connection(conn)
                        print("1.View books list \n2.Search book \n ")
                        choice = eval(input("Enter your choice \n"))
                        if choice == 1:
                            view_books()
                        elif choice == 2:
                            search_book()
                        else:
                            print("INVALID INPUT\n")
                    else:
                        print("INVALID PASSWORD")
                        close_connection(conn)
                if f == 0:
                    print("INVALID USERNAME\n")
                    close_connection(conn)
        elif ch == 2:
            s_reg()
    else:
        print("INVALID CHOICE")