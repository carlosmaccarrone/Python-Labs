import sqlite3
import datetime

con = sqlite3.connect("deudores.db", detect_types=sqlite3.PARSE_DECLTYPES|sqlite3.PARSE_COLNAMES)
cur = con.cursor()
cur.execute("create table deudores(ID INTEGER, FECHA TEXT, DNI INTEGER, CARTERA TEXT, PAGO TEXT, PLAN TEXT, CUOTA INTEGER, MONTO INTEGER, CANAL_PAGO TEXT, POR INTEGER, HONORA TEXT, IVA TEXT, A_RENDIR TEXT, REND TEXT, FECHA2 TEXT, OP TEXT, FAC TEXT, N_de_operacion INTEGER, N_de_sucursal INTEGER, SUCURSAL TEXT, IMP TEXT, OBSERVACION TEXT, BANCO TEXT, TRAMO TEXT)")





#today = datetime.date.today()
#now = datetime.datetime.now()

#cur.execute("insert into test(d, ts) values (?, ?)", (today, now))
#cur.execute("select d, ts from test")
#row = cur.fetchone()
#print today, "=>", row[0], type(row[0])
#print now, "=>", row[1], type(row[1])

#cur.execute('select current_date as "d [date]", current_timestamp as "ts [timestamp]"')
#row = cur.fetchone()
#print "current_date", row[0], type(row[0])
#print "current_timestamp", row[1], type(row[1])
