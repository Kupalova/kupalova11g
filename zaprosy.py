import sqlite3
data = sqlite3.connect('kupalova_bd.db')
cur = data.cursor()
#1) Получение таблицы с именем, логином и id всех пользователей отсортированные по дате регистрации
for row in cur.execute('SELECT имя, логин, id FROM пользователь ORDER BY дата_регистрации DESC'):
    print(*row)
print()

#2) Получение имени пользователя который делал данные заказы, даты заказов, id заказа и итоговая сумма
for row in cur.execute('SELECT order_id, адрес, дата,(SELECT имя FROM пользователь WHERE id = customer_id) as customer_id, сумма FROM заказ'):
    print(*row)
print()

#3) Делаем то же самое что во 2, но при это сортируем по сумме заказа
for row in cur.execute('SELECT order_id,адрес, дата, (SELECT имя FROM пользователь WHERE id = customer_id) as customer_id, сумма FROM заказ WHERE сумма >300'):
    print(*row)
print()
#4) сравнение 2 таблиц пользователя и заказа
for row in cur.execute('SELECT * FROM пользователь CROSS JOIN заказ;'):
    print(*row)
print()

#5) Получение таблицы корзины, где вместо id товара и пользователя - название товара и имя пользователя
for row in cur.execute('SELECT (SELECT имя FROM пользователь WHERE id = customer_id) as customer_id, (SELECT название FROM товар WHERE id = item_id) as "название товара", цена,количество FROM корзина'):
    print(*row)