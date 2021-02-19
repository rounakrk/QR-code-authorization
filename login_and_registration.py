import psycopg2
from enc_dec import encrypt_pass, decrpyt_pass
from qrcode_gen import qrcode_generation
from main import img_mode


def connect():
    conn = psycopg2.connect(
        database='my_db',
        user='postgres', password='postgres', host='localhost', port='5432',
    )
    return conn


def starting(cursor):
    # Doping EMPLOYEE table if already exists.
    cursor.execute("DROP TABLE IF EXISTS EMPLOYEE_QR")

    # Creating table as per requirement
    sql = '''CREATE TABLE EMPLOYEE_QR(
    EMP_ID VARCHAR(20) PRIMARY KEY,
    NAME VARCHAR(20) NOT NULL,
    EMAIL VARCHAR(30) NOT NULL UNIQUE,
    PASSWORD TEXT NOT NULL,
    PASSKEY TEXT NOT NULL)
    '''
    cursor.execute(sql)
    print("Table created successfully........")


def insert(cursor, table, columns, values):
    '''Function to insert the form data 'values' into table 'table'
    according to the columns in 'column' '''

    # connection = psycopg2.connect('dbname=Birds', 'user=robert')
    # mark = connection.cursor()
    statement = 'INSERT INTO ' + table + ' (' + columns + ') VALUES (' + values + ')'
    cursor.execute(statement)
    print("Insert into Table successfully........")
    print("Profile created. \nWelcome "+values[1][1:-1]+" you can use login now !")
    return True
    # connection.commit()
    # return


def signup_web(l):
    conn = connect()
    cursor = conn.cursor()

    f = ['emp_id', 'name', 'email', 'password']
    # l = []
    # for i in f:
    #     print("Enter" + i + ":", end="")
    #     l.append(input())

    table = "EMPLOYEE_QR"
    columns = "EMP_ID, NAME, EMAIL, PASSWORD, PASSKEY"
    emp_id = "EMP"+str(int(last_row()[3:])+1)
    name = l[0]
    email = l[1]
    ps, key = encrypt_pass(l[2])
    values = "'" + emp_id + "'" + ", " + "'" + name + "'" + ", " + "'" + email + "'" + ", " + "'" + ps + "'" + ", " + "'" + key + "'"
    if insert(cursor, table, columns, values):
        conn.commit()
        conn.close()
        qrcode_generation(emp_id, emp_id)
        return True

    # Commit your changes in the database
    

def login_web(cred):
    conn = connect()
    cursor = conn.cursor()
    # print("Enter your email :", end="")
    email = cred[0]
    # print("Enter your password :", end="")
    password = cred[1]

    sql = "select * from employee_qr where email = " + "'" + email + "';"
    cursor.execute(sql)
    records = cursor.fetchall()
    if records:
        for i in records:
            emp_id = i[0]
            name = i[1]
            pswd = i[3]
            key = i[4]

        dec_msg = decrpyt_pass(key, pswd)
        if password == dec_msg:
            # print("Welcome " + name)
            return [name, emp_id]
        #     print("Do you want your QR image for verfication : (y/n)")
        #     ans = input()
        #     if ans == 'y':
        #         qrcode_generation(emp_id, emp_id)
        #     else:
        #         print("As you wish !!")

        # else:
        #     print("Wrong password !!")

    else:
        return False
        # print("Wrong Credentials")
    conn.close()


def qr_login():
    # qr images\EMP1011.png
    print("Enter the path of the image file with file name :")
    path = input()
    qr_data = img_mode(path)
    # qr_data = "EMP1020"
    if qr_data:
        conn = connect()
        cursor = conn.cursor()
        sql = "select * from employee_qr where emp_id = " + "'" + qr_data + "';"
        cursor.execute(sql)
        records = cursor.fetchall()
        if records:
            for i in records:
                emp_id = i[0]
                name = i[1]
            print("Welcome " + name)
            # print(records)
        else:
            print("False data")

def showall():
    conn = connect()
    cursor = conn.cursor()
    sql = " select * from employee_qr; "
    cursor.execute(sql)
    records = cursor.fetchall()
    print(records)

def last_row():
    conn = connect()
    cursor = conn.cursor()
    sql = " select * from employee_qr order by emp_id desc limit 1; "
    cursor.execute(sql)
    records = cursor.fetchall()
    for i in records:
        emp_id = i[0]
        break
    return emp_id

# if __name__ == "__main__":
#     conn = connect()
#     cursor = conn.cursor()
#     print("Enter your choice as per the number in front :")
#     print("1. Sign In \n2. Sig Up")
#     ans = int(input())
#     if ans == 1:
#         print("Do you wish to sign in using QR code authorization ? (y/n)")
#         ans = input()
#         if ans == 'y':
#             qr_login()
#             # showall()
#         else:
#             login()
#     elif ans == 2:
#         signup()
#     else:
#         print("Pick the correct number as your response !!")

#     # Commit your changes in the database
#     conn.commit()

#     # Closing the connection
#     conn.close()

# if __name__ == "__main__":
#     last_row()