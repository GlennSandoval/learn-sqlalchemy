"""
Joined Table Inheritance
"""
from sqlalchemy import Column, Integer, String, ForeignKey

from db import Base


class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    type = Column(String)

    __mapper_args__ = {
        'polymorphic_identity': 'employee',
        'polymorphic_on': type
    }

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (
            self.name, self.fullname, self.nickname)


class Admin(User):
    __tablename__ = 'admins'
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    admin_title = Column(String(30))

    __mapper_args__ = {
        'polymorphic_identity': 'admin',
    }

    def __repr__(self):
        return "<Admin(name='%s', fullname='%s', nickname='%s', admin_title='%s')>" % (
            self.name, self.fullname, self.nickname, self.admin_title)


class Moderator(User):
    __tablename__ = 'moderators'
    id = Column(Integer, ForeignKey('users.id'), primary_key=True)
    moderator_name = Column(String(30))

    __mapper_args__ = {
        'polymorphic_identity': 'moderator',
    }

    def __repr__(self):
        return "<Moderator(name='%s', fullname='%s', nickname='%s', moderator_name='%s')>" % (
            self.name, self.fullname, self.nickname, self.moderator_name)
