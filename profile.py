import sqlite3
def getProfile(id):
    con=sqlite3.connect("Face.db")
    sql="SELECT * FROM people WHERE id="+str(id)
    data=con.execute(sql)
    profile=None
    for row in data:
        profile=row
    con.close()
    return profile

