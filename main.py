import psycopg2
import numpy
from BondModel import BondModel
from config import *


def add_bond(ticker, count_of_bonds) -> None:
    global cur
    global conn
    bd = BondModel(ticker)
    query_for_main_info = "INSERT INTO bonds_information VALUES (%s, %s, %s, %s, %s, %s)"

    try:
        cur.execute(f"select * from bonds_information where ticker = \'{bd.sec_id}\'")
        rows = cur.fetchall()
        if len(rows) != 0:
            cur.execute(f"update bonds_information set bonds_count = bonds_count + {count_of_bonds} where ticker = \'{bd.sec_id}\'")
        else:
            cur.execute(query_for_main_info,
                        (bd.sec_id, bd.name, bd.current_price, bd.coupon_value, count_of_bonds, bd.coupon_frequency))
            for i in bd.get_coupon_frequency():
                cur.execute(
                    f"INSERT INTO frequency_of_payment2 (bonds_ticker, month_of_payment) VALUES (\'{bd.sec_id}\',\'{i}\')")

        conn.commit()

    except Exception as err:
        print("[INFO] database error", err)


def delete_bond(ticker, count_of_bonds) -> None:
    global conn
    global curr
    bd = BondModel(ticker)
    try:
        cur.execute(f"select bonds_count from bonds_information where ticker = \'{bd.sec_id}\'")
        rows = cur.fetchall()
        if rows[0][0] <= count_of_bonds:
            cur.execute(f"delete from frequency_of_payment2 where bonds_ticker = \'{bd.sec_id}\'")
            cur.execute(f"delete from bonds_information where ticker = \'{bd.sec_id}\'")
        else:
            cur.execute(f"update bonds_information set bonds_count = bonds_count - {count_of_bonds} where ticker = \'{bd.sec_id}\'")

        conn.commit()
    except Exception as err:
        print("[INFO] database error", err)


def show_all_bonds(): #вывод
    global conn
    global cur
    cur.execute(f"select * from bonds_information")
    rows = cur.fetchall()
    print(rows[0])

conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)
cur = conn.cursor()

add_bond('RU000A100D89', 1)
# delete_bond('RU000A107043', 5)
print("Hello World")
cur.close()
conn.close()



