from models.config import connection

def is_register(user_name, password):
    conn = connection()
    with conn.cursor() as cursor:
        query = f"SELECT * FROM customers WHERE user_name = '{user_name}' AND password = '{password}';"
        cursor.execute(query)
        res = cursor.fetchone()
        if res:
            return True
        return False

def add_user(new_username, new_password):
    conn = connection()
    with conn.cursor() as cursor:
        query = f"INSERT INTO customers (user_name, password) VALUES ('{new_username}', '{new_password}');"
        cursor.execute(query)
        conn.commit()

def is_admin(username, password):
    conn = connection()
    with conn.cursor() as cursor:
        query = f"SELECT * FROM customers WHERE user_name = '{username}' AND password = '{password}' AND user_name = 'Manager' AND password = '123456';"
        cursor.execute(query)
        result = cursor.fetchone()
    return result is not None


def search_user_by_name(new_user_name):
    conn = connection()
    with conn.cursor() as cursor:
        query = f"SELECT * FROM customers WHERE user_name = '{new_user_name}';"
        cursor.execute(query)
        res = cursor.fetchone()
        if res:
            return True
        return False
