import Gate,datetime
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


Gate.gate()

UserOp = input(""" """)
