import mysql.connector

f = open('Table.csv')
fString = f.read()

fList = []
for line in fString.split('\n'):
    fList.append(line.split(','))

print(fList)


import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='GLPadmin',
    database='glp_table_db',
    buffered = True
)
print(mydb)


cursor = mydb.cursor()
cursor.execute('SHOW DATABASES')

Position = fList[0][0]
Team = fList[0][1]
GP = fList[0][2]
W = fList[0][3]
D = fList[0][4]
L = fList[0][5]
GS = fList[0][6]
GC = fList[0][7]
GD = fList[0][8]
Pts = fList[0][9]

queryCreateTable = """CREATE TABLE GLPTABLE_NEW(
                    {} int(2) not null,
                    {} varchar(255) not null,
                    {} int(2) not null,
                    {} int(2) not null,
                    {} int(2) not null,
                    {} int(2) not null,
                    {} int(2) not null,
                    {} int(2) not null,
                    {} int(3) not null,
                    {} int(3) not null
                    )""".format(Position, Team, GP, W, D, L, GS, GC, GD, Pts)

cursor.execute(queryCreateTable)

