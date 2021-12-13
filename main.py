import os

from db import Session, engine, Base
from employee import Employee, Manager
from user import User, Admin


def clear_sqlite_db():
    if os.path.exists("data.db"):
        os.remove("data.db")


if __name__ == '__main__':
    clear_sqlite_db()
    Base.metadata.create_all(engine)
    # Joined Table Inheritance
    with Session() as session:
        test_user = User(name="Dave", fullname="Davothy", nickname="Sam")
        test_admin = Admin(name="Sam", fullname="Samantha", nickname="Stinky", admin_title="The Destroyer")
        session.add(test_user)
        session.add(test_admin)
        session.commit()
        our_user = session.query(User).filter_by(name='Dave').first()
        our_admin = session.query(Admin).filter_by(name='Sam').first()
    print(our_user)
    print(our_admin)

    # Concrete Table Inheritance
    with Session() as session:
        test_employee = Employee(name="George")
        test_manager = Manager(name="Greg", manager_data="lacks toes and tolerant")
        session.add(test_employee)
        session.add(test_manager)
        session.commit()
        our_user = session.query(Employee).filter_by(name='George').first()
        our_admin = session.query(Manager).filter_by(name='Greg').first()
    print(our_user)
    print(our_admin)
