from utils import connect_to_db

def insert_item(name, quantity_type_id, quantity_value):
	query = """
	INSERT INTO items (name, quantity_type_id, quantity_value, bought)
	VALUES (%s, %s, %s, FALSE)
	"""
	with connect_to_db() as (conn, cursor):
		cursor.execute(query, (name, quantity_type_id, quantity_value))
		conn.commit()

def get_items(bought=False):
	query = """
	SELECT id, name, quantity_type_id, quantity_value, bought
	FROM items
	WHERE bought = %s
	"""
	with connect_to_db() as (conn, cursor):
		cursor.execute(query, (bought,))
		items = cursor.fetchall()
	return items

def mark_item_as_bought(item_id):
	query = """
	UPDATE items
	SET bought = TRUE
	WHERE id = %s
	"""
	with connect_to_db() as (conn, cursor):
		cursor.execute(query, (item_id,))
		conn.commit()