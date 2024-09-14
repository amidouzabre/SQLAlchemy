from sqlalchemy import create_engine
from models import Base

db_path = 'sqlite:///test_alchemy.db'

engine = create_engine(db_path)

try:
    conn = engine.connect()
    print("Success")
    # Create ours tables
    Base.metadata.create_all(bind=conn)
except Exception as ex:
    print(ex)