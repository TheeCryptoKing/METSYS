from sqlalchemy.orm import DeclarativeBase,Mapped,mapped_column,relationship
from sqlalchemy import ForeignKey

class Base(DeclarativeBase):
    pass

class Player(Base):
    __tablename__ = 'player'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=True)
    location_id:Mapped[int] = mapped_column(primary_key=True)
    
    location:Mapped[str["Location"]] = relationship(back_populates='player')
    enemy:Mapped[str["Enemy"]] = relationship(back_populates='player')

class Location(Base):
    __tablename__ = 'location'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=True)
    players:Mapped[str["Player"]] = relationship(back_populates='location')
    enemies:Mapped[str["Enemy"]] = relationship(back_populates='location')

class Enemy(Base):
    __tablename__ = 'enemy'
    id:Mapped[int] = mapped_column(primary_key=True)
    name:Mapped[str] = mapped_column(nullable=True)
    location_id:Mapped[int] = mapped_column(primary_key=True)
    
    location:Mapped[str["Location"]] = relationship(back_populates='enemy')
    player_id:Mapped[int] = mapped_column(ForeignKey('player.id'),nullable=False)
    
    players:Mapped[str["Player"]] = relationship(back_populates='enemy')
    