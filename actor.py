
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Actor(Base):
    __tablename__ = 'actor'

    id = Column(Integer, primary_key=True)
    nombre = Column(String)
    nacionalidad = Column(String)
    biografia=Column(String)
    peliculas = relationship("Pelicula", back_populates="actor")

    def __init__(self, nombre,nacionalidad, biografia):
        self.nombre = nombre
        self.nacionalidad=nacionalidad
        self.biografia=biografia