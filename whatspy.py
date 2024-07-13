import Gate,datetime,time
import Upload

def time_hour():

    dt = datetime.datetime.now().time()
    dt = str(dt)
    dth = dt[0:2]

    return dth


def time_minute():
    dt = datetime.datetime.now().time()
    dt = str(dt)
    dtm = dt[3:5]

    return dtm


h=time_hour()
m=time_minute()


#Gate.gate()
time.sleep(.5)
print("Note:Be careful in filling Inputs !!")
time.sleep(.5)
UserOp = input("""Menu:
                
                1# Create 
                2# Upload
                3# Exit\n
                
                ==>""")
while UserOp not in ["1", "2", "3"]:
    print("Invalid input")
    time.sleep(.5)
    UserOp = input("""Menu:

                    1# Create 
                    2# Upload
                    3# Exit\n

                    ==>""")

if UserOp == "3":
    print("Process Exited >>.")

elif UserOp == "1":
    NoOfStd = input("How many records do you need to Upload ?(In digits) :")
    while NoOfStd.isalpha():
        print("Invalid Input")
        NoOfStd = int(input("How many records do you need to Upload ?(In digits) :"))
    NoOfStd = int(NoOfStd)
    for x in range(NoOfStd):
        print(f"Record {x+1}")
        Upload.upload()
        time.sleep(1)
        print("Upload Successful")


