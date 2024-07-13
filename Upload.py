import pymysql,time

SqlCon = pymysql.connect(host='localhost', user="root", password='$6h#9l@2', database='whatspy_server')

SqlCur = SqlCon.cursor()


def upload():

    EntryPass = 0
    Check = 0

    SqlCur.execute("Select * From whatspy_std;")

    RecordCheck = SqlCur.fetchall()

    while Check == 0:
        StudentName = input("StudentName: ")
        print("Class need to be given in Numbers")
        Class = input("Class: ")
        PhoneNumber = input("PhoneNumber: +91 ")
        TabVal = (StudentName.capitalize(), Class, "+91" + PhoneNumber)

        if StudentName.isalpha() and Class.isdigit() and PhoneNumber.isdigit() and len(PhoneNumber) == 10 and \
                Class in [str(x+1) for x in range(12)] and TabVal not in RecordCheck:

            SqlCur.execute(f'Insert into whatspy_std Value' + str(TabVal) + ';')
            SqlCon.commit()
            Check = 1
        elif TabVal in RecordCheck:
            print("Record already exists")

        else:
            print("Found Mistake In Input Data")

