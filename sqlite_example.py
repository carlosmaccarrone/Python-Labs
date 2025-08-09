from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)

engine = create_engine('sqlite:///:memory:', echo=True)
Session = sessionmaker(bind=engine)
session = Session()

Base.metadata.create_all(engine)

# Crear y agregar un usuario
new_user = User(name='Charly', email='charly@example.com')
session.add(new_user)
session.commit()

# Consultar
user = session.query(User).filter_by(name='Charly').first()

print("\nLITTLE DATABASE RESULTS")
print(user.name, user.email)