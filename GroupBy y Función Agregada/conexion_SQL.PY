import pyodbc as py

conne = py.connect('DRIVER={SQL Server};SERVER=10.10.10.254;DATABASE=ISSSTE_VER_DSBB;UID=sa;PWD=Ul1979_*')
print(conne)

print("Conectado Correctamente")

cursor = conne.cursor()

query = """
        SELECT O.id, O.timestamp_date, O.timestamp_hour, O.patient_relationship,
               W.type, W.start_time W.active 
               FROM offers O
               INNER JOIN work_session W 
               ON O.work_session_id = W.id"""

cursor.execute(query)

# nombres de columnas
columnas = [column[0] for column in cursor.description]
print(columnas)

rows = cursor.fetchall()

for row in rows:
    print(row)