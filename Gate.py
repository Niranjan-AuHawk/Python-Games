def gate():

    import pymysql,time

    SqlCon = pymysql.connect(host='localhost', user="root", password='$6h#9l@2', database='Personal_server')

    SqlCur = SqlCon.cursor()

    print("HELLO...WELCOME TO 'WhatPy 0.1' ")
    time.sleep(1)
    print("Automate You Mark Uploading in Whatsapp")
    time.sleep(1)
    print("Loading..")
    time.sleep(2.0)
    print("""

                        #1 -> Sign Up
                        #2 -> Login 
                    \n""")

    Entry = input("===>")
    while Entry != "1" and Entry != "2":
        print("Invalid Input")
        print("""

                            #1 -> Sign Up
                            #2 -> Login 
                        """)

        Entry = input("===>")

    EntryPass = 0
    Check = 0

    SqlCur.execute("Select UserName From BattleTank_Login_Info;")

    UserCheck = SqlCur.fetchall()

    SqlCur.execute("Select * From BattleTank_Login_Info;")

    RecordCheck = SqlCur.fetchall()

    if Entry == "1":
        print("Sign Up--> \n")
        Username = input("UserName: ")
        Password = input("Password: ")
        Email = input("Email: ")
        TabVal = (Username, Email, Password)
        UserTup = (Username,)

        while Check == 0:

            if 8 <= len(
                    Password) <= 12 and "@" in Email and Username != "" and UserTup not in UserCheck and TabVal not in \
                    RecordCheck:
                TabVal = (Username, Email, Password)
                UserTup = (Username,)
                SqlCur.execute(f'Insert into BattleTank_Login_Info Value' + str(TabVal) + ';')
                SqlCon.commit()
                print("Sign In Successful")
                Check = 1
            else:
                if Username == "":
                    print("Username Should NOT Be Empty !! ")
                    Username = input("UserName:")

                elif Username.isdigit():
                    print("Username NEED To Be a Combination of Letters and Numbers !! ")
                    Username = input("UserName:")

                elif TabVal in RecordCheck:
                    print("The Same Details Found. Try Login!!")

                elif UserTup in UserCheck:
                    print("Username Already Taken!!")
                    Username = input("UserName:")
                    UserTup = (Username,)

                elif "@" not in Email or "gmail.com" not in Email:
                    print("""Invalid Email !!
                     hint:'@'or'gmail.com'""")
                    Email = input("Email:")

                elif len(Password) < 8 or len(Password) > 12:
                    print("The Length of the Password SHOULD Be 8 to 12 Character!!")
                    Password = input("Password:")

                else:
                    print("Please CHECK All Details")
                    Username = input("UserName:")
                    Password = input("Password:")
                    Email = input("Email:")

                Check = 0



    else:
        print("Login--> ")
        Username = input("UserName:")
        Password = input("Password:")
        Email = input("Email:")
        TabVal = (Username, Email, Password)
        UserTup = (Username,)

        while Check == 0:
            TabVal = (Username, Email, Password)
            UserTup = (Username,)

            if 8 <= len(Password) <= 12 and "@" in Email and Username != "" and UserTup in UserCheck and TabVal in \
                    RecordCheck:
                print("Login In Successful")
                Check = 1
            else:
                if Username == "":
                    print("Username Should NOT Be Empty !! ")
                    Username = input("UserName:")

                elif Username.isdigit():
                    print("Username NEED To Be a Combination of Letters and Numbers !! ")
                    Username = input("UserName:")

                elif TabVal not in RecordCheck:
                    print("The Details Not Found. Try Sign Up!!")
                    Username = input("UserName:")
                    Password = input("Password:")
                    Email = input("Email:")

                elif UserTup not in UserCheck:
                    print("Username Not Found!!")
                    Username = input("UserName:")
                    UserTup = (Username,)

                elif "@" not in Email or "gmail.com" not in Email:
                    print("""Invalid Email !!
                     hint:'@'or'gmail.com'""")
                    Email = input("Email:")

                elif len(Password) <= 8 or len(Password) >= 12:
                    print("The Length of the Password SHOULD Be 8 to 12 Character!!")
                    Password = input("Password:")

                else:
                    print("Please CHECK All Details")
                    Username = input("UserName:")
                    Password = input("Password:")
                    Email = input("Email:")

                Check = 0
    print(f"Hello {Username}.Nice to Meet You(^.^)")
