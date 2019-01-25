import sqlite3

db = sqlite3.connect('sqltest.db')
ptr = db.cursor()
QUERY="INSERT INTO test VALUES (NULL, "

print("Ingrese nombre")
a = raw_input()
print("Ingrese DNI")
b = raw_input()

ptr.execute(QUERY + "'" + a + "', " + b + ")")
print(QUERY + "'" + a + "', " + b + ")")

db.commit()
db.close()
