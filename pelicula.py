
from sqlalchemy import Column, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

from base import Base


class Pelicula(Base):
    __tablename__ = 'pelicula'

    id = Column(Integer, primary_key=True)
    titulo = Column(String)
    duracion = Column(Integer)
    pais=Column(String)

    actor_id = Column(Integer, ForeignKey('actor.id'))
    actor = relationship("Actor", back_populates="peliculas")

    def __init__(self, titulo, duracion, pais):
        self.titulo = titulo
        self.duracion = duracion
        self.pais = pais