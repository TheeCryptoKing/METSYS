from sqlalchemy.orm import declarative_base, relationship
from sqlalchemy import Column, ForeignKey, Integer, Float, String, create_engine

engine = create_engine('sqlite:///game.db', echo=True)
Base = declarative_base()

class Location(Base):
    __tablename__ = 'location'
    # MVP = FF, Guild, Home
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    player = relationship("Player", back_populates='location')
    enemies = relationship("Enemy", back_populates='location')

class Player(Base):
    __tablename__ = 'player'
    # STRETCH xp, hp, defense, attack, Agility 
    # MVP, Moves, Strength, Speed,  
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    # player.location can change location 
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship("Location", back_populates='player')
    abilities_id = Column(Integer, ForeignKey('abilities.id'))
    abilities = relationship("Abilities", back_populates='player')
    # Player Stats
    Strength = Column(Integer)
    Speed = Column(Integer)
    Weapon = Column(String, nullable=True)
    hp = Column(Float, default=100)
    xp = Column(Integer, default=0)
    # STRETCH wallet:[int] = mapped_column(Integer, default=0)
    # abilities = relationship("Abilities", back_populates="player")


class Enemy(Base):
    # hp, xp given, Int, Speed, Strength, 
    __tablename__ = 'enemy'
    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=True)
    # enemy.location can change enemy location 
    location_id = Column(Integer, ForeignKey('location.id'))
    location = relationship("Location", back_populates='enemy')
    abilities_id = Column(Integer, ForeignKey('abilities.id'))
    abilities = relationship("Abilities", back_populates='enemy')
    # Enemy Stats
    hp = Column(Float, default=100)
    xp_given = Column(Integer)
    intellect = Column(Integer)
    speed = Column(Integer)
    strength = Column(Integer)
    weapon = Column(String, nullable=True)
    
    
    
# class Abilities(Base):
#     # one-to-one
#     __tablename__ = 'ability'
#     id = Column(Integer, primary_key=True)
#     ability_name = Column(String)
    # weapon_ability = Column(String, default=None)
    # companion_ability = Column(String, default=None)
    # player_id = Column(Integer, ForeignKey('player.id'), nullable=False)
    # player = relationship("Player", back_populates='abilities')
    # enemy = relationship("Enemy", back_populates='')


