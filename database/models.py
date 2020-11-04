import os
from sqlalchemy import Column, String, Integer
from flask_sqlalchemy import SQLAlchemy
import json

database_filename = "database.db"
project_dir = os.path.dirname(os.path.abspath(__file__))
database_path = "sqlite:///{}".format(os.path.join(project_dir, database_filename))

db = SQLAlchemy()

'''
setup_db(app)
    binds a flask application and a SQLAlchemy service
'''
def setup_db(app):
    app.config["SQLALCHEMY_DATABASE_URI"] = database_path
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)


'''
db_drop_and_create_all()
    drops the database tables and starts fresh
    can be used to initialize a clean database
    !!NOTE you can change the database_filename variable to have multiple verisons of a database
'''
def db_drop_and_create_all():
    db.drop_all()
    db.create_all()


'''
Movie
Movies with attributes title and release date
'''
class Movie(db.Model):
    __tablename__ = 'movies'
    # Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    title = Column(String(240), nullable=False)
    release_date = Column(String(180), nullable=False)

    '''
    insert()
        inserts a new model into a database
        the model must have a ia, name and release_date
        EXAMPLE
            movie = movie(title=req_title, release_date=req_release_date)
            movie.insert()
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a model from a database
        the model must exist in the database
        EXAMPLE
            movie = Movie.query.filter(Movie.id == id).one_or_none()
            movie.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            movie = Movie.query.filter(Movie.id == id).one_or_none()
            movie.title = 'Spider man'
            movie.update()
    '''
    def update(self):
        db.session.commit()

    def details(self):
        return {
            'id': self.id,
            'title': self.title,
            'release_date': self.release_date
        }

    def __repr__(self):
        return json.dumps(self.short())


'''
Movie
Movies with attributes title and release date
'''
class Actor(db.Model):
    __tablename__ = 'actors'
    # Autoincrementing, unique primary key
    id = Column(Integer().with_variant(Integer, "sqlite"), primary_key=True)
    name = Column(String(180), nullable=False)
    age = Column(Integer(), nullable=False)
    gender = Column(String(180), nullable=False)

    '''
    insert()
        inserts a new model into a database
        the model must have a name, age, gender
        EXAMPLE
            actor = Actor(name=req_name, age=req_age, gender=req_gender)
            actor.insert()
    '''
    def insert(self):
        db.session.add(self)
        db.session.commit()

    '''
    delete()
        deletes a model from a database
        the model must exist in the database
        EXAMPLE
            actor = Actor.query.filter(Actor.id == id).one_or_none()
            actor.delete()
    '''
    def delete(self):
        db.session.delete(self)
        db.session.commit()

    '''
    update()
        updates a new model into a database
        the model must exist in the database
        EXAMPLE
            actor = Actor.query.filter(Actor.id == id).one_or_none()
            actor.name = 'James'
            actor.update()
    '''
    def update(self):
        db.session.commit()

    def details(self):
        return {
            'id': self.id,
            'name': self.name,
            'age': self.age,
            'gender': self.gender
        }

    def __repr__(self):
        return json.dumps(self.short())
