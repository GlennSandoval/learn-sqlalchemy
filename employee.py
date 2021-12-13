"""
Concrete Table Inheritance
"""
from sqlalchemy import Column, Integer, String

from db import Base

"""
Two critical points should be noted:

 - We must define all columns explicitly on each subclass, even those of the same name. A column such as Employee.name here is not copied out to the tables mapped by Manager or Engineer for us.

 - while the Engineer and Manager classes are mapped in an inheritance relationship with Employee, they still do not include polymorphic loading. Meaning, if we query for Employee objects, the manager and engineer tables are not queried at all.

"""


class Employee(Base):
    __tablename__ = 'employee'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))

    def __repr__(self):
        return "<Employee(name='%s')>" % self.name


class Manager(Employee):
    __tablename__ = 'manager'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    manager_data = Column(String(50))

    __mapper_args__ = {
        'concrete': True
    }

    def __repr__(self):
        return "<Manager(name='%s', manager_data='%s')>" % (
            self.name, self.manager_data)


class Engineer(Employee):
    __tablename__ = 'engineer'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    engineer_info = Column(String(50))

    __mapper_args__ = {
        'concrete': True
    }

    def __repr__(self):
        return "<Engineer(name='%s', engineer_info='%s')>" % (
            self.name, self.fullname)
