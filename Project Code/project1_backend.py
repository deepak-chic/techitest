import mysql.connector


# import project1_frontend

def empData():
    con = mysql.connector.connect(host="localhost", user="root", passwd="root", database="project")
    cur = con.cursor()

    cur.execute(
        "CREATE TABLE IF NOT EXISTS employee(id integer primary key AUTO_INCREMENT,empID text ,Firstname text,Surname text,DoB text,Age text,Gender text,Address text,Mobile text)")
    con.commit()
    con.close()

def addStdRec(empID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    con = con = mysql.connector.connect(host="localhost", user="root", passwd="root")
    cur = con.cursor()
    cur.execute("use project")
    cur.execute("INSERT INTO employee VALUES(NULL,%s,%s,%s,%s,%s,%s,%s,%s)",
                (empID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    con.commit()
    con.close()


def viewData():
    con = con = mysql.connector.connect(host="localhost", user="root", passwd="root")
    cur = con.cursor()
    cur.execute("use project")
    cur.execute("select * from employee")
    row = cur.fetchall()
    con.close()
    return row


def deleteRec(id):
    con = con = mysql.connector.connect(host="localhost", user="root", passwd="root")
    cur = con.cursor()
    cur.execute("use project")
    cur.execute("DELETE FROM employee WHERE id=%s", (id,))
    con.commit()
    con.close()


def searchData(empID, Firstname, Surname, DoB, Age, Gender, Address, Mobile):
    con = con = mysql.connector.connect(host="localhost", user="root", passwd="root")
    cur = con.cursor()
    cur.execute("use project")
    cur.execute(
        "SELECT * FROM employee WHERE empID=%s or Firstname=%s or Surname=%s or DoB=%s or Age=%s or Gender=%s or Address=%s or Mobile=%s",
        (empID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    rows = cur.fetchall()
    con.close()
    return rows


def dataUpdate(id, empID="", Firstname="", Surname="", DoB="", Age="", Gender="", Address="", Mobile=""):
    con = mysql.connector.connect(host="localhost", user="root", passwd="root")
    cur = con.cursor()
    cur.execute("use project")
    cur.execute(
        "UPDATE srkanth SET empID=%s,Firstname=%s,Surname=%s,DoB=%s,Age=%s,Gender=%s,Address=%s,Mobile=%s WHERE id=%s",
        (empID, Firstname, Surname, DoB, Age, Gender, Address, Mobile))
    con.commit()
    con.close()    