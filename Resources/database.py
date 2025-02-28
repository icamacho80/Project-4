import sqlite3
import pandas as pd
csv_file = "real-estate-data.csv"

df = pd.read_csv(csv_file)

dbfile = "housing_price.db"
conn = sqlite3.connect(dbfile)

df.to_sql("housing_price", conn, if_exists="replace", index=False)
cursor = conn.cursor()
cursor.execute('''DROP TABLE housing_price''')
cursor.execute('''CREATE TABLE IF NOT EXISTS housing_price(
brokered_by VARCHAR,
status VARCHAR,
price VARCHAR,
bed VARCHAR,
bath VARCHAR,
acre_lot VARCHAR,
street VARCHAR,    
city VARCHAR,
state VARCHAR,
zip_code VARCHAR,
house_size VARCHAR,
prev_sold_date VARCHAR 
);
               ''')

cursor.execute('''select * from housing_price''')
print(cursor.fetchall())

conn.commit()
conn.close()

print(f"CSV '{csv_file}' successfully converted to SQLite database '{dbfile}'!")