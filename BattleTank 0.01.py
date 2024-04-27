import pymysql, time, random

SqlCon = pymysql.connect(host='localhost', user="root", password='$6h#9l@2', database='Personal_server')

SqlCur = SqlCon.cursor()


class Tank(object):

    def __init__(self, name):
        self.name = name
        self.Life = 200
        self.Ammo = 20
        self.Shield = 3
        self.Alive = True
        self.Point = 3
        self.Boom = 1

    def info(self):
        print(f"{self.name} have {self.Life} Lives, {self.Ammo} Ammo, {self.Shield} Shields and {self.Point} Points")

    def is_alive(self):
        if self.Alive:
            print(f"""Your Tank is Alive with Lives<{self.Life}> Shield<{self.Shield}> Ammo<{self.Ammo}>""")
        else:
            print("Your Death")

    def loss_life(self,):
        if self.Life == 0:
            self.Alive = False
        else:
            self.Life -= 15
            self.Alive = True

    def loss_life2(self):
        self.Life -= 40
        print("Your Boomed!")

    def hit(self, enemy):
        self.Ammo -= 1
        enemy.loss_life()

    def has_ammo(self):
        if self.Ammo != 0:
            if self.Ammo < 5:
                print(f"You have {self.Ammo} Ammo Left, So it is Better to Buy Some")
            else:
                print(f"You Have Much Enough For Now. {self.Ammo} Ammo")
        else:
            print("The Ammo Is Completely Over, Buy Some Fast!!! ")
            return False

    def buy_ammo(self):
        self.Point -= 1
        self.Ammo += 1
        print("Purchase Successful")

    def gain_points(self):
        self.Point += 5
        print("Got A Point")

    def shield_of(self, myself):
        self.Shield -= 1
        if myself.loss_life():
            self.Life += 15
        else:
            self.Life += 40
        print("On Guard")

    def buy_shield(self):
        self.Point -= 4
        self.Shield += 1
        print("Purchase Successful")

    def buy_boom(self):
        self.Point -= 8
        self.Boom += 1
        print("Purchase Successful")

    def launch_boom(self, enemy):
        self.Boom -= 1
        enemy.loss_life2()
        print("Got Something Better For You..(^O^)..")


print("HELLO...WELCOME TO 'TANK BATTLE 0.1' ")
print("EASY AND FUN A GAME!!")
print("JOIN THE FUN(^o^)")
print("""

                    #1 -> Sign Up
                    #2 -> Login 
                """)

Entry = input("===>")
while Entry != "1" and Entry != "2":
    print("Invalid Input")
    print("""

                        #1 -> Sign Up
                        #2 -> Login 
                    """)

    Entry = input("===>")

EntryPass = 0
Check = 1

SqlCur.execute("Select UserName From BattleTank_Login_Info;")

UserCheck = SqlCur.fetchall()

SqlCur.execute("Select * From BattleTank_Login_Info;")

RecordCheck = SqlCur.fetchall()

if Entry == "1":
    print("Sign Up--> ")
    Username = input("UserName:")
    Password = input("Password:")
    Email = input("Email:")
    TabVal = (Username, Email, Password)
    UserTup = (Username,)

    while Check == 0:

        if 8 <= len(Password) <= 12 and "@" in Email and Username != "" and UserTup not in UserCheck and TabVal not in \
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
FirstTime = input("Is it Your First Time Playing This Game? Y/N ")
if FirstTime.upper() == "YES" or FirstTime.upper() == "Y":
    FirstTime = True
    Rules = ["How to play:",
             "->You will be Fighting with 4 more Players.You can also Customizes the Number of Players.",
             "->Each Player are Given a Chance to Either Attack Others or Defend Themselves.",
             "->All the players a Bots.There is no bias in the game, Bots are using Random function to attack players.",
             "So It will be a Fair and Square Game.",
             "->The Rounds will be Taken place Till There is a Single Winner.",
             "->By killing each Player You Gain 5 points and You can use to buy Ammo, Shield and Boom.",
             "->We Wish to a Good Luck For you Match"]
    for x in Rules:
        print(x)
        time.sleep(2)
else:
    pass
PlayersCount = 5


def player_selection(level):
    player_selected = random.randint(1, 10)
    if player_selected > level:
        return True
    else:
        return False


GameInput = int(input("""Select Your Choice:

                            1 -> Start
                            2 -> Edit Players
                            3 -> Difficulty
                            4 -> Exit 

    =>"""))
while GameInput != 1:

    if GameInput == 2:
        CLoop = True
        while CLoop:
            Count = input("Players Count:")
            if 3 <= int(Count) <= 8:
                PlayersCount = int(Count)
                CLoop = False
            elif Count.isalnum():
                print("Player Count need to be a digit")
            else:
                print("The Player Count Need to be in a Limit of 3 To 8.Your Input Invalid")

    elif GameInput == 3:
        Mode = int(input("""
                            1 -> Easy
                            2 -> Medium 
                            3 -> Hard 

        =>
        """))
        if Mode == 1:
            player_selection(3)
            print("Easy Mode Activated ")
        elif Mode == 2:
            player_selection(5)
            print("Medium Mode Activated ")
        elif Mode == 3:
            player_selection(5)
            print("Hard Mode Activated ")

    elif GameInput == 4:
        print("Just try this game Later...BYE(^.^)")
        break

    else:
        print("Invalid Input!!")

    GameInput = int(input("""Select Your Choice:

                                    1 -> Start
                                    2 -> Edit Players
                                    3 -> Difficulty
                                    4 -> Exit 


        =>"""))
if GameInput == 1:
    TotalPlayers = {"You": Tank("You"), "Player1": Tank("Player1"), "Player2": Tank("Player2"),
                    "Player3": Tank("Player3"), "Player4": Tank("Player4"), "Player5": Tank("Player5"),
                    "Player6": Tank("Player6"), "Player7": Tank("Player7"), "Player8": Tank("Player8")}
    You = TotalPlayers["You"]
    Player1 = TotalPlayers['Player1']
    Player2 = TotalPlayers['Player2']
    Player3 = TotalPlayers['Player3']
    Player4 = TotalPlayers['Player4']
    Player5 = TotalPlayers['Player5']
    Player6 = TotalPlayers['Player6']
    Player7 = TotalPlayers['Player7']
    Player8 = TotalPlayers['Player8']
    PlayersIn = {1: You, 2: Player1, 3: Player2, 4: Player3, 5: Player4, 6: Player5, 7: Player6, 8: Player7, 9: Player8}
    TotalPlayersKeys = list(TotalPlayers.keys())
    PlayersInValues = list(PlayersIn.values())
    PlayersName = []
    Players = {}
    AllInfo = ""
    for x in range(PlayersCount):
        PlayersName.append(TotalPlayersKeys[x])
        Players.setdefault(x+1, PlayersInValues[x])
    PlayersKeys = list(Players.keys())
    print(PlayersName)
    print(PlayersKeys)
    print("Let's Start the game(^.^)")
    StartGame = 0
    en = input("PRESS ENTER")
    while StartGame == 0:
        for Player in PlayersKeys:
            if Player == 1:
                PlayerInput = int(input("""
                    #1 -> Shoot
                    #2 ->
                    
                    ==>"""))
                while PlayerInput != 1:
                    if PlayerInput == 2:
                        pass
                if PlayerInput == 1:
                    for i in range(1, len(Players)):

                        print(f"#{i} -> {PlayersName[i]}, Health={Players[i].Life}")
                        time.sleep(1)
                    PlayerSelected = int(input("==>"))
                    while PlayerSelected not in PlayersKeys:
                        print("Invalid Input")
                        for i in range(1, len(Players)):
                            print(f"#{i} -> {PlayersName[i]}, Health ={Players[i].Life} ")
                            time.sleep(1)
                        PlayerSelected = int(input("==>"))
                    print(f"You:Haha... Shoot You Down {PlayersName[PlayerSelected]} ")
                    Players[Player].hit(Players[PlayerSelected])
                    print(Players[PlayerSelected].Life)
                    pass

else:
    pass
