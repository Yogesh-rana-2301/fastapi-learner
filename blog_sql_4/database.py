from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHAMY_DATABASE_URL = 'sqlite:///./new.db.sqlite3'

engine = create_engine(SQLALCHAMY_DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(bind=engine,autoflush=False,autocommit=False)
                            
base=declarative_base()



def get_db():
    db=SessionLocal()
    try:
        yield(db)   
    finally:
        db.close()
