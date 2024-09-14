from sqlalchemy import create_engine

db_path = 'sqlite:///test_alchemy.db'

engine = create_engine(db_path)

try:
    conn = engine.connect()
    print("Success")
except Exception as ex:
    print(ex)