from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.models import Base

DATABASE_URL = "postgresql://postgres:Asdqwe!23@localhost:5432/fastapi_users"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def create_tables():
    Base.metadata.create_all(bind=engine)


if __name__ == "__main__":
    create_tables()
    print("Tables created")