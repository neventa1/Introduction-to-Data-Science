import psycopg2
import csv
conn = psycopg2.connect("dbname=history user=postgres")
cur = conn.cursor()



cur.execute("SELECT 'brand' FROM gas_station;")
cur.execute("SELECT COUNT (DISTINCT brand) FROM gas_station;")
#print(cur.fetchall())
#Distinct Fetches every value only once
cur.execute("SELECT DISTINCT brand FROM gas_station ORDER BY brand;")
brands = cur.fetchall()
#for i,j  in enumerate(brands):
#    print(i, j)

def get_max_price(gas_type, month, year):
    if month < 10:
        month = "0" + str(month)
    print(gas_type, month, year)
    cur.execute("SELECT MAX(%s) FROM gas_station_information_history WHERE EXTRACT(MONTH FROM date) = %s and EXTRACT(YEAR FROM date) = %s;" % (gas_type, month, year))
    res = cur.fetchone()
    print(res[0])
    return res[0]


def get_min_price(gas_type, month, year):
    if month < 10:
        month = "0" + str(month)
    print(gas_type, month, year)
    #NULLIF removes 0 and -1 from table
    #cur.execute("SELECT MIN(NULLIF(NULLIF(NULLIF(%s, 888), 0), -1)) as minprice FROM gas_station_information_history GROUP BY MONTH(date);" % (gas_type, month, year) )
    cur.execute("SELECT extract(month from date) FROM gas_station_information_history;" )

    res = cur.fetchall()
    print(res)
    return res[0]


list_max_diesel = []
list_max_e10 = []
list_max_e5 = []

start_date = (6,2018)
end_date = (7,2018)

date = start_date

with open('min_price.csv', 'a') as csvfile:
    csvwriter = csv.writer(csvfile, delimiter=' ',
                            quotechar='|', quoting=csv.QUOTE_MINIMAL)
    csvwriter.writerow(['Date', 'E5', 'E10', 'Diesel'])
    while date != end_date:
        print(date)
        max_diesel = get_min_price('diesel', date[0], date[1])
        max_e5 = get_min_price('e5', date[0], date[1])
        max_e10 = get_min_price('e10', date[0], date[1])
        csvwriter.writerow([date, max_diesel, max_e5, max_e10])
        csvfile.flush()
        if date[0] == 12:
            date = (1, date[1]+1)
        else:
            date = (date[0]+1, date[1])
