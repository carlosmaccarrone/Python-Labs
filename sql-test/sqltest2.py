import sqlite3

db = sqlite3.connect('sqltest.db')
ptr = db.cursor()
QUERY="INSERT INTO test (ID,Nombre,DNI) VALUES (NULL, ?, ?);"

print("Ingrese nombre")
a = raw_input()
print("Ingrese DNI")
b = raw_input()

ptr.execute(QUERY,(str(a), b))
print(QUERY,(str(a), b))

db.commit()
db.close()
