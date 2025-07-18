from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Note(Base):
    __tablename__ = "notes"

    id = Column(Integer, primary_key=True, index = True)
    title = Column(String, nullable=False)
    is_completed = Column(Boolean, default=False)