import psycopg2
from BondModel import BondModel
from config import *

conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)
cur = conn.cursor()
bd = BondModel('RU000A104YT6')
count_of_bonds = 3 # Количество облигаций

bd.show_full_info()
query_for_calendar = f"INSERT INTO frequency_of_payment (bond_tickers, {', '.join(bd.get_coupon_frequency())})" \
                     f" VALUES (\'{bd.sec_id}\'{len(bd.get_coupon_frequency()) * ', TRUE'});"



query_for_main_info = "INSERT INTO bonds_information VALUES (%s, %s, %s, %s, %s, %s)"

try:
    cur.execute(query_for_main_info, (bd.sec_id, bd.name, bd.current_price, bd.coupon_value, count_of_bonds, bd.coupon_frequency))
    print(query_for_main_info)

    for i in bd.get_coupon_frequency():
        print(f"INSERT INTO frequency_of_payment2 (bonds_ticker, month_of_payment) VALUES (\'{bd.sec_id}\',\'{i}\')")
        cur.execute(f"INSERT INTO frequency_of_payment2 (bonds_ticker, month_of_payment) VALUES (\'{bd.sec_id}\',\'{i}\')")

    conn.commit()

except Exception as err:
    print("[INFO] database error", err)

finally:
    cur.close()
    conn.close()
