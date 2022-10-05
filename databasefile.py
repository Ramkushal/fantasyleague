#created by P.Ram kushal reddy
#write data base name in xxxx
databasename = "xxxx.db"
import sqlite3
db=sqlite3.connect(databasename)
cur=db.cursor()
cur.execute('''CREATE TABLE match (
Player TEXT (50) PRIMARY KEY,
Scored INTEGER,
Faced INTEGER,
Fours INTEGER,
Sixers INTEGER,
Bowled INTEGER,
Maiden INTEGER,
Given INTEGER,
Wkts INTEGER,
Catches INTEGER,
Stumpings INTEGER,
RO INTEGER);''')
cur.execute('''CREATE TABLE teams (
    name TEXT (50) PRIMARY KEY,
    players TEXT (500),
    value INTEGER);''')
cur.execute('''CREATE TABLE stats (
    Player TEXT (50),
    matches INTEGER,
    runs INTEGER,
    Hundreds INTEGER,
    Fifties INTEGER,
    value INTEGER,
    ctg TEXT (10));''')
x=[
"'Kohli',102,98,8,2,0,0,0,0,0,0,1",
"'Yuvraj',12,20,1,0,48,0,36,1,0,0,0",
"'Rahane',49,75,3,0,0,0,0,0,1,0,0",
"'Dhawan',32,35,4,0,0,0,0,0,0,0,0",
"'Dhoni',56,45,3,1,0,0,0,0,3,2,0",
"'Axar',8,4,2,0,48,2,35,1,0,0,0",
"'Pandya',42,36,3,3,30,0,25,0,1,0,0",
"'Jadeja',18,10,1,1,60,3,50,2,1,0,1",
"'Kedar',65,60,7,0,24,0,24,0,0,0,0",
"'Ashwin',23,42,3,0,60,2,45,6,0,0,0",
"'Umesh',0,0,0,0,54,0,50,4,1,0,0",
"'Bumrah',0,0,0,0,60,2,49,1,0,0,0",
"'Bhuvaneshwar',15,12,2,0,60,1,46,2,0,0,0",
"'Rohit',46,65,5,1,0,0,0,0,1,0,0",
"'Karthik',29,42,3,0,0,0,0,0,2,0,1"
]
y=[
"'Kohli',189,8257,29,43,120,'BAT'",
"'Yuvraj',86,3589,10,21,100,'BAT'",
"'Rahane',158,5435,11,31,100,'BAT'",
"'Dhawan',25,565,2,1,85,'AR'",
"'Dhoni',78,2573,3,19,75,'BAT'",
"'Axar',67,208,0,0,100,'BWL'",
"'Pandya',70,77,0,0,75,'BWL'",
"'Jadeja',16,1,0,0,85,'BWL'",
"'Kedar',111,675,0,1,90,'BWL'",
"'Ashwin',136,1914,0,10,100,'AR'",
"'Umesh',296,9496,10,64,110,'WK'",
"'Bumrah',73,1365,0,8,60,'WK'",
"'Bhuvaneshwar',17,289,0,2,75,'AR'",
"'Rohit',304,8701,14,52,85,'BAT'",
"'Karthik',11,111,0,0,75,'AR'"
]
for i in range(15):
    sql1="INSERT INTO stats (Player,matches,runs,Hundreds,Fifties,value,ctg) VALUES ({});".format(y[i])
    sql="INSERT INTO match (Player, Scored, Faced, Fours, Sixers, Bowled, Maiden, Given, Wkts, Catches, Stumpings, Ro) VALUES ({});".format(x[i])
    try:
        cur=db.cursor()
        cur.execute(sql)
        cur.execute(sql1)
        db.commit()
        print ("one record added successfully")
    except:
        print ("error in operation")
        db.rollback()
db.close()
