from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from player import *


if __name__ == '__main__':
    engine = create_engine('sqlite:///game.db')
    Session = sessionmaker(bind=engine)
    session = Session()
    print("this db is awakend")

    import ipdb; ipdb.set_trace()