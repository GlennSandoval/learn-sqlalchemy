from db import Session, engine, Base
from user import User

if __name__ == '__main__':
    Base.metadata.create_all(engine)
    with Session() as session:
        test_user = User(name="Dave", fullname="Davothy", nickname="Sam")
        session.add(test_user)
        session.commit()
        our_user = session.query(User).filter_by(name='Dave').first()
    print(our_user)
