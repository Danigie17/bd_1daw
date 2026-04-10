import psycopg2

conn = psycopg2.connect(
    host='localhost',
    database='ventas',
    user='postgres',
    password='2765',
    port='5432',
    sslmode='require'
)

                        
cur = conn.cursor()
cur.execute("insert into pedido values (38, 1000, '10/03/2016', 1, 5);")
conn.commit
cur.close()
conn.close()