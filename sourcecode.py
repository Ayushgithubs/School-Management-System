
#SOURCE CODE FOR School Management.
print ("****STUDENT MANAGEMENT SYSTEM****")
#creating database
import mysql.connector # type: ignore
mydb=mysql.connector.connect(host="localhost", user="root",passwd="123456")
mycursor=mydb.cursor()
mycursor.execute("create database if not exists school_mng")
mycursor.execute("use school_mng")
#creating required tables 
mycursor.execute("create table if not exists student(adminno int primary key, sname varchar(10),class int(5),mobileno char(10),Fees varchar(6))")
mycursor.execute("create table if not exists teacher(empno int primary key, tname varchar(10),subject varchar(9),mobileno int(10),salary int(6))")
mydb.commit()

def last_sid():
    try:
        mycursor.execute("select max(adminno) from student")
        i=mycursor.fetchone()
        a=int(i[0])
        return a
    except:
        b=1
        return b
def last_tid():

    try:
        mycursor.execute("select * from teacher order by empno desc limit 1")
        for i in mycursor:
            r=i[0]
        return r
    except:
        b=1
        return b
    
while(True):
    
    print("1=Add student")
    print("2=Delete student")
    print("3=Add teacher")
    print("4=Delete teacher")
    print("5=Search student")
    print("6=Search teacher")
    print("7=Exit")
    ch=int(input("Enter your choice:"))
    
#PROCEDURE FOR CREATING A NEW ACCOUNT OF THE APPLICANT
    if(ch==1):
        print("All information prompted are mandatory to be filled")
        d=int(last_sid())+1
        name=input("Enter sname(limit 35 characters):")
        Class=input("Enter class:")
        mn=input("Enter mobile no.:")
        s=str(input("Enter Fees true/false:"))
        mycursor.execute("insert into student values('"+str(d)+"','"+name+"','"+Class+"','"+mn+"','"+s+"')")
        #insert into student values((select max(adminno) from student alias)+1,"test","1","1","true");
        mydb.commit()
        print("Student record is successfully created!!!")
    elif(ch==3):
        f=int(last_sid())+1
        dp=str(input("Enter Teacher name:"))
        dot=str(input("Enter subject: "))
        n=input("Enter mobile no.:")
        nm=input("Enter salary:")
        mycursor.execute("insert into teacher values('"+str(f)+"','"+str(dp)+"','"+dot+"','"+str(n)+"','"+str(nm)+"')")
        mydb.commit()
        print("Teacher added successully!!!")

    elif(ch==2):
        acno=str(input("Enter admission number:"))
        mycursor.execute("delete from student where adminno= "+acno)
        mydb.commit()
        print("Successfully Deleted student.")
        
    elif(ch==4):
        acno=str(input("Enter Emplyoee number:"))
        mycursor.execute("delete from teacher where empno= "+acno)
        mydb.commit()
        print("Successfully Deleted teacher")
    elif(ch==5):
        n=str(input("Enter Name:"))
        mycursor.execute("select * from student where sname='"+n+"'")
        for i in mycursor:
               print(i)
    elif(ch==6):
        n=str(input("Enter Name:"))
        mycursor.execute("select * from teacher where tname='"+n+"'")
        for i in mycursor:
               print(i)
    else:
         break
