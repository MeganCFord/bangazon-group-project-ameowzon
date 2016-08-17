from objects.customer_object import *
from utility.utility import *
import sqlite3


def generate_new_customer(name="", address="", city="", state="", zipcode="", phone=""):
    """
    Adds a new customer based on the input generated by menu prompts, then requests the newly created autoincremented customer primary key to set as 'current customer' in meow.py.
    ===========
    Method Arguments: strings. 1. file_name of txt file to add to, 2. name, 3. address, 4. city, 5. state, 6. zipcode, 7. phone. Note that these are keyed arguments so can be passed in any order if specified with the appropriate key.
    Returns: integer of current customer.
    """
    with sqlite3.connect("bangazon.db") as database:
        db = database.cursor()

        db.execute("""INSERT INTO Customer (FullName, StreetAddress, City, StateOfResidence, ZipCode, PhoneNumber)
                        VALUES (?,?,?,?,?,?)""",
                    (name, address, city, state, zipcode, phone))
        database.commit()

        db.execute("select c.CustomerId from Customer c where c.FullName = ?", (name,))
        thing = db.fetchone()
        return thing[0], name


def get_customer_name(customer_id):
    """
    Queries the database for the name of the customer the user selects in the meow.py menu.
    ========
    Method Arguments: the id of the selected customer.
    Returns: string name of the selected customer.
    """
    with sqlite3.connect("bangazon.db") as database:
        db = database.cursor()

    db.execute("""SELECT c.FullName
                    FROM Customer c
                    WHERE c.CustomerId = ?""", [customer_id])
    thing = db.fetchone()
    return thing[0]


def generate_customer_menu():
    """
    Queries bangazon.db's customer table and returns a list of tuples for each active customer. The first item in each tuple is the unique customer ID, the second is the customer's full name. This list will be printed in utility.py.
    ============
    Method Arguments: None.
    Returns: list of two-item tuples.
    """

    with sqlite3.connect("bangazon.db") as database:
        db = database.cursor()

        db.execute("""SELECT c.CustomerId, c.FullName
                        FROM Customer c""")
        return db.fetchall()
