from sqlalchemy import create_engine

engine = create_engine("postgresql+psycopg2://tracker_user:tracker_pass@localhost:5432/expense_db")

try:
    connection = engine.connect()
    print("Successfully connected to database")
    connection.close()
except Exception as e:
    print("Connection error:", e)