import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='GLPadmin',
    database='GLP_table_db',
    buffered= True
)
print(mydb)


cursor = mydb.cursor()
cursor.execute('SHOW DATABASES')


def updateTeam(hteam, ateam, hscore, ascore):
    query = "SELECT * FROM glptable_new;"
    cursor.execute(query)
    set_round = 19
    hGD = hscore - ascore
    aGD = ascore - hscore
    if hscore > ascore:
        hquery = "UPDATE glptable_new SET GP = %s, Pts = Pts+%s, W = W+1, GS = GS+%s, GC = GC+%s, GD = GD+%s WHERE Team = %s"
        hdata_tuple = (set_round, 3, hscore, ascore, hGD, hteam)
        cursor.execute(hquery, hdata_tuple)

        aquery = "UPDATE glptable_new SET GP = %s, Pts = Pts+%s, L = L+1, GS = GS+%s, GC = GC+%s, GD = GD+%s WHERE Team = %s"
        adata_tuple = (set_round, 0, ascore, hscore, aGD, ateam)
        cursor.execute(aquery, adata_tuple)

        mydb.commit()
    elif hscore == ascore:
        query = "UPDATE glptable_new SET GP = %s, Pts = Pts+1, D = D+1, GS = GS+%s, GC = GC+%s, GD = GD+%s WHERE Team = %s"


        hdata_tuple = (set_round, hscore, ascore, hGD, hteam)
        cursor.execute(query, hdata_tuple)
        adata_tuple = (set_round, ascore, hscore, aGD, ateam)
        cursor.execute(query, adata_tuple)

        mydb.commit()
    elif hscore < ascore:
        hquery = "UPDATE glptable_new SET GP = %s, Pts = Pts+%s, L = L+1, GS = GS+%s, GC = GC+%s, GD = GD+%s WHERE Team = %s"

        hdata_tuple = (set_round, 0, hscore, ascore, hGD, hteam)
        cursor.execute(hquery, hdata_tuple)

        aquery = "UPDATE glptable_new SET GP = %s, Pts = Pts+%s, W = W+1, GS = GS+%s, GC = GC+%s, GD = GD+%s WHERE Team = %s"

        adata_tuple = (set_round, 3, ascore, hscore, aGD, ateam)
        cursor.execute(aquery, adata_tuple)

        mydb.commit()

updateTeam("Rioni", "Amkal", 0, 3)
updateTeam("Algeti", "Dinamo Tbilisi", 8, 9)
updateTeam("Gardabani", "Blancos United", 6, 5)
updateTeam("Melomania", "Zugdidi", 5, 3)
updateTeam("Saburtalo", "Zenit", 6, 1)
updateTeam("Rubin", "Shark Team", 3, 0)