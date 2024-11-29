import logging
from utils import connect_to_db

logging.basicConfig(level=logging.INFO)

class ShoppingListService:
    def add_item(self, name, quantity, quantity_type_id):
        with connect_to_db() as (conn, cursor):
            try:
                cursor.execute(
                    "INSERT INTO items (name, quantity, quantity_type_id) VALUES (%s, %s, %s)",
                    (name, quantity, quantity_type_id)
                )
                conn.commit()
                logging.info(f"Item '{name}' added successfully.")
            except Exception as e:
                logging.error(f"Error adding item: {e}")
                conn.rollback()

    def get_items_to_buy(self):
        with connect_to_db() as (conn, cursor):
            try:
                cursor.execute("SELECT id, name, quantity, quantity_type_id FROM items WHERE bought = FALSE")
                items = cursor.fetchall()
                return items
            except Exception as e:
                logging.error(f"Error fetching items to buy: {e}")
                return []

    def get_bought_items(self):
        with connect_to_db() as (conn, cursor):
            try:
                cursor.execute("SELECT id, name, quantity, quantity_type_id FROM items WHERE bought = TRUE")
                items = cursor.fetchall()
                return items
            except Exception as e:
                logging.error(f"Error fetching bought items: {e}")
                return []

# Example usage
if __name__ == "__main__":
    service = ShoppingListService()
    service.add_item("Milk", 2, 3)  # Assuming 3 is the id for 'liter'
    to_buy = service.get_items_to_buy()
    bought = service.get_bought_items()
    print("Items to buy:", to_buy)
    print("Bought items:", bought)