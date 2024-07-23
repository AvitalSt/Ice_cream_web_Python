from models.config import connection

def get_all_ice():
    conn = connection()
    with conn.cursor() as cursor:
        query = f"SELECT * FROM ice_cream;"
        cursor.execute(query)
        res = cursor.fetchall()
        return res
        
def add_ice_cream(name, dis, priceO, priceK, img):
    conn = connection()
    with conn.cursor() as cursor:
        query = """
        INSERT INTO ice_cream (ice_cream_name, descraption, price_per_ball, price_per_kilo, img)
        VALUES (?, ?, ?, ?, ?)
        """
        cursor.execute(query, (name, dis, priceO, priceK, img))
        conn.commit()

def get_ice_cream_by_id(id):
    conn = connection()
    try:
        with conn.cursor() as cursor:
            query = "SELECT * FROM ice_cream WHERE id_ice_cream=?;"
            cursor.execute(query, (id))
            res = cursor.fetchone()
        return res
    finally:
        conn.close()

def search_ice_cream(search_query):
    conn = connection()
    with conn.cursor() as cursor:
        query = "SELECT * FROM ice_cream WHERE ice_cream_name LIKE ?"
        cursor.execute(query, (search_query + '%'))
        return cursor.fetchall()
