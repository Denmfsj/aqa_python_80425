from sqlalchemy import Column, Integer, String
from core.db.tables.orm_base_table import Base



class OrmUser(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, unique=True)
    age = Column(Integer, nullable=False)

    def __str__(self):
        return f'id={self.id}, name={self.name}, age={self.age}'