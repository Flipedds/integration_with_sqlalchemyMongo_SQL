from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.orm import relationship
from sqlalchemy import Column, create_engine, inspect, select, func
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import ForeignKey

Base = declarative_base()


class User(Base):
    __tablename__ = "user_account"
    # atributos
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id},name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True)
    email_address = Column(String(30), nullable=False)
    user_id = Column(Integer, ForeignKey("user_account.id"), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"


print(User.__tablename__)
print(Address.__tablename__)

# conexão com o banco de dados
engine = create_engine("sqlite://")

# criando as classes com tabelas no banco de dados
Base.metadata.create_all(engine)

# investiga o esquema do banco de dados
inspetor_engine = inspect(engine)
print(inspetor_engine.has_table("user_account"))
print(inspetor_engine.get_table_names())
print(inspetor_engine.default_schema_name)

with Session(engine) as session:
    filipe = User(
        name='filipe',
        fullname='filipe andre',
        address=[Address(email_address='filipea@email.com')]
    )
    sandy = User(
        name='sandy',
        fullname='sandy cardoso',
        address=[Address(email_address='sandy@email.br'),
                 Address(email_address='sandy@email.org')]
    )
    patrick = User(name='patrick', fullname='patrick cardoso')

    # enviando para o bd
    session.add_all([filipe, sandy, patrick])

    session.commit()

stmt = select(User).where(User.name.in_(['filipe', 'sandy', 'patrick']))
print('Recuperando usuários a partir de condição de filtragem')
for user in session.scalars(stmt):
    print(user)

# select
stmt_address = select(Address).where(Address.user_id.in_([2]))
print('\nRecuperando os endereços de email de sandy')
for address in session.scalars(stmt_address):
    print(address)

# order by
stmt_order = select(User).order_by(User.fullname.desc())
print('\nRecuperando info de maneira ordenada')
for result in session.scalars(stmt_order):
    print(result)

stmt_join = select(User.fullname, Address.email_address).join_from(Address, User)
print('\nRecuperando info juntando resultados')
for result in session.scalars(stmt_join):
    print(result)

connection = engine.connect()
results = connection.execute(stmt_join).fetchall()
print("\nExecutando statement a partir da connection")
for result in results:
    print(result)

stmt_count = select(func.count('*')).select_from(User)
print('\n Total de instâncias em User')
for result in session.scalars(stmt_count):
    print(result)

# encerrando a session
session.close()
