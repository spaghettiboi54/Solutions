"""
Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Anvend det, du har lært i dette kapitel om databaser, på en første opgave.

Trin 1:
Opret en ny SQLite database "S2311_my_second_sql_database.db" i din solutions mappe.
Denne database skal indeholde 2 tabeller.
Den første tabel skal hedde "customers" og repræsenteres i Python-koden af en klasse kaldet "Customer".
Tabellen bruger sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "name", "address" og "age".
Definer selv fornuftige datatyper for attributterne.

Trin 2:
Den anden tabel skal hedde "products" og repræsenteres i Python-koden af en klasse kaldet "Product".
Denne tabel bruger også sin første attribut "id" som primærnøgle.
De andre attributter i tabellen hedder "product_number", "price" og "brand".

Trin 3:
Skriv en funktion create_test_data(), der opretter testdata for begge tabeller.

Trin 4:
Skriv en metode __repr__() for begge dataklasser, så du kan vise poster til testformål med print().

Til læsning fra databasen kan du genbruge de to funktioner select_all() og get_record() fra S2240_db_class_methods.py.

Trin 5:
Skriv hovedprogrammet: Det skriver testdata til databasen, læser dataene fra databasen med select_all() og/eller get_record() og udskriver posterne til konsollen med print().

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

from sqlalchemy.orm import declarative_base, Session  # install sqlalchemy with the command "pip install SQLAlchemy" in a terminal.
from sqlalchemy import Column, String, Integer  # the library sqlalchemy helps us to work with a database
from sqlalchemy import create_engine, select

Database = 'sqlite:///S2311_my_second_sql_database.db'
Base = declarative_base()



class Customers(Base):
    __tablename__ = "customers"
    def __repr__(self):
        return f"customer(id: {self.id} name: {self.name} address: {self.address} age: {self.age}"
    id = Column(Integer, primary_key=True)
    name = Column(String)
    address = Column(String)
    age = Column(Integer)


class Products(Base):
    __tablename__ = "products"
    def __repr__(self):
        return f"product(id: {self.id} product number: {self.product_number} price: {self.price} brand: {self.brand}"
    id = Column(Integer, primary_key=True)
    product_number = Column(Integer)
    price = Column(Integer)
    brand = Column(String)



def create_test_data():
    with Session(engine) as session:
        new_items = []
        new_items.append(Customers(name="Daniel", address="new mexico", age=17))
        new_items.append(Customers(name="John", address="Groove street", age=5))
        new_items.append(Products(product_number=0, price=50, brand="scratchy's workshop"))
        new_items.append(Products(product_number=1, price=50, brand="Abibas"))
        session.add_all(new_items)
        session.commit()


def get_by_id(classparam, record_id):
    with Session(engine) as session:
        return session.scalars(select(classparam).where(classparam.id == record_id)).first()

def select_all(classparam):
    with Session(engine) as session:
        record = session.scalars(select(classparam))
        result = []
        for i in record:
            result.append(i)
    return result


engine = create_engine(Database, echo=False, future=True)
Base.metadata.create_all(engine)

print("all customers")
print(select_all(Customers))
print("product with id 1")
print(get_by_id(Products, 1))



