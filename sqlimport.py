import json
import mysql.connector

with open('tesco.json', 'r') as f:
    data = json.load(f)

# print(data)

try:
    connection = mysql.connector.connect(
        user='root',
        password='Asdf1234',
        host='localhost',
        port=3306,
        database='stock_price'
    )
    if connection.is_connected():
        print('Connected!')
except Exception as e:
    print("Cannot connect!")

cur = connection.cursor()

time_series_data = data[0]["Time Series (Daily)"]

for date_str, values in time_series_data.items():
    open_price = float(values['1. open'])
    high_price = float(values['2. high'])
    low_price = float(values['3. low'])
    close_price = float(values['4. close'])
    volume = int(values['5. volume'])

    sql = "insert into tesco_price (date, open, high, low, close, volume)VALUES(%s, %s, %s, %s,%s,%s)"
    cur.execute(sql, (date_str, open_price, high_price,
                      low_price, close_price, volume))

connection.commit()
connection.close()

print("Data inserted successfully into MySQL table.")
