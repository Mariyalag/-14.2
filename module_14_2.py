import sqlite3

connection = sqlite3.connect("not_telegram2.db")
cursor = connection.cursor()

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')

cursor.execute("CREATE INDEX IF NOT EXISTS idx_email ON Users (email)")

cursor.execute("DELETE FROM Users")

for i in range(1, 11):
    cursor.execute(" INSERT INTO Users (username, email, age, balance) VALUES (?, ?, ?, ?)",
                   (f"User{i}", f"example{i}@gmail.com", i * 10, 1000))

cursor.execute("UPDATE Users SET balance = 500 WHERE id % 2 = 1")

cursor.execute("DELETE FROM Users WHERE id % 3 = 1")

# cursor.execute("SELECT username, email, age, balance FROM Users")
cursor.execute("SELECT username, email, age, balance FROM Users WHERE age != 60")

cursor.execute("DELETE FROM Users WHERE id = ?", (6,))

cursor.execute("SELECT COUNT(*) FROM Users")
total_users = cursor.fetchone()[0]
cursor.execute("SELECT SUM(balance) FROM Users")
all_balances = cursor.fetchone()[0]

# cursor.execute("SELECT AVG(balance) FROM Users")
# avg_balance = cursor.fetchone()[0]
# print(f"Средний баланс всех пользователей: {avg_balance}")

print(f"Общее количество пользователей: {total_users}")
print(f"Сумма всех балансов: {all_balances}")
print(f"Cредний баланс всех пользователей: {all_balances / total_users}")

# users = cursor.fetchall()
# for user in users:
#     print(f"Имя: {user[0]} | Почта: {user[1]} | Возраст: {user[2]} | Баланс: {user[3]}")

connection.commit()
connection.close()