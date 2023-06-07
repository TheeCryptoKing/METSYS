from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Float, String, create_engine

engine = create_engine('sqlite:///game.db', echo=True)
Base = declarative_base()
Base.metadata.create_all(engine)

# model.py
class Location(Base):
    __tablename__ = 'location'
    # MVP = FF, Guild, Home
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    player = relationship("Player", back_populates='location')
    enemy = relationship("Enemy", back_populates='location')


class Player(Base):
    __tablename__ = 'player'
    # MVP, Moves, Strength, Speed,  
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    
    # player.location can change location 
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship("Location", foreign_keys=[location_id], back_populates='player')
    
    # player moves
    primary_attack = Column(Integer, ForeignKey('abilities.id'))
    attack1 = relationship("Abilities", foreign_keys=[primary_attack], back_populates='player2')
    secondary_attack = Column(Integer, ForeignKey('abilities.id'))
    attack2 = relationship("Abilities", foreign_keys=[secondary_attack], back_populates='player3')
    
    # Player Stats
    Strength = Column(Integer)
    Speed = Column(Integer)
    Weapon = Column(String, nullable=True)
    hp = Column(Float, default=100)
    intellect = Column(Integer, default=0)
    xp = Column(Integer, default=0)
    # STRETCH wallet:[int] = mapped_column(Integer, default=0)

class Enemy(Base):
    # hp, xp given, Int, Speed, Strength, 
    __tablename__ = 'enemy'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    
    # enemy.location can change enemy location 
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship("Location", foreign_keys=[location_id], back_populates='enemy')
    
    # Enemy moves
    # primary_attack = Column(Integer, ForeignKey('abilities.id'))
    # attack1 = relationship("Abilities", foreign_keys=[primary_attack], back_populates='enemy2')
    # secondary_attack = Column(Integer, ForeignKey('abilities.id'))
    # attack2 = relationship("Abilities", foreign_keys=[secondary_attack], back_populates='enemy3')
    
    # Enemy Stats
    hp = Column(Float, default=100)
    xp_given = Column(Integer)
    intellect = Column(Integer)
    speed = Column(Integer)
    strength = Column(Integer)
    weapon = Column(String, nullable=True)
    
class Abilities(Base):
    # one-to-one
    __tablename__ = 'abilities'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    # Player bidemnsional route
    player2 = relationship("Player", foreign_keys=[Player.primary_attack], back_populates='attack1')
    player3 = relationship("Player", foreign_keys=[Player.secondary_attack], back_populates='attack2')
    
    # enemy2 = relationship("Enemy", foreign_keys=[Enemy.primary_attack], back_populates='attack1')
    # enemy3 = relationship("Enemy", foreign_keys=[Enemy.secondary_attack], back_populates='attack2')
    


    
    




