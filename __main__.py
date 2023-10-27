from actor import Actor
from pelicula import Pelicula
from base import session_factory

def crear_actor():
    session = session_factory()

    nombre=input('ingrese el nombre del actor ')
    nacionalidad=input('ingrese la nacionalidad del actor ')
    biografia=input('ingrese la biografía del actor ')

    el_actor=Actor(nombre, nacionalidad,biografia)
    session.add(el_actor)
    session.commit()
    session.close()

def consultar_actores():
    session = session_factory()
    actores = session.query(Actor)
    session.close()
    for i in actores:
        print(f'- id {i.id} nombre {i.nombre} nacionalidad {i.nacionalidad} biografia {i.biografia}')

def actualizar_actor():
    session = session_factory()
    print('cual actor desea modificar?')
    consultar_actores()
    identificador=int(input('ingrese el id del actor que desea modificar'))
    nombre=input('ingrese el nombre del actor ')
    nacionalidad=input('ingrese la nacionalidad del actor ')
    biografia=input('ingrese la biografía del actor ')


    session.query(Actor).filter(Actor.id == identificador).update(
        {
            "nombre": nombre,
            "nacionalidad": nacionalidad,
            "biografia": biografia,
        }
    )
    actor=session.query(Actor).filter(Actor.id == identificador).one()
    
    print(f'- id {actor.id} nombre {actor.nombre} nacionalidad {actor.nacionalidad} biografia {actor.biografia}')
    print('registro actualizado con éxito !!')

    session.commit()
    session.close()

    #https://github.com/auth0-blog/sqlalchemy-orm-tutorial/blob/master/examples/basic/__main__.py
    




    
if __name__ == "__main__":
    print('Actores......')

    while True:
        print('que desea hacer?')
        print('1. ver actores')
        print('2. crear un nuevo actor')
        print('3. modificar un actor')
        respuesta=input('ingrese una opción ')
        if respuesta=='1':
            consultar_actores()
        elif respuesta=='2':
            crear_actor()
        elif respuesta=='3':
            actualizar_actor()
    