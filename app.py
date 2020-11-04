import os
import sys
from flask import Flask, request, jsonify, abort
from sqlalchemy import exc, and_
import json
from flask_cors import CORS
from database.models import db_drop_and_create_all, setup_db, Movie, Actor
from auth.auth import AuthError, requires_auth

app = Flask(__name__)
setup_db(app)
CORS(app)

# For first time runner and testing
db_drop_and_create_all()


# ROUTES
@app.route('/', methods=['GET'])
def entry_point():
    return jsonify({
        'success': True,
        'content': "casting API Capstone project"
    })

# Get actors list
@app.route('/actors', methods=['GET'])
@requires_auth('get:actors')
def get_actors(payload):
    actors = Actor.query.order_by(Actor.id).all()
    if not actors:
        abort(404)
    actors_details = []
    for actor in actors:
        actors_details.append(actor.details())

    return jsonify({
        'success': True,
        'actors': actors_details
    })

# Get movie details
@app.route('/movies', methods=['GET'])
@requires_auth('get:movies')
def get_movies(payload):
    movies = Movie.query.order_by(Movie.id).all()
    if not movies:
        abort(404)
    movies_details = []
    for movie in movies:
        movies_details.append(movie.details())
    return jsonify({
        'success': True,
        'movies': movies_details
    })

# Add actor to db
@app.route('/actors', methods=['POST'])
@requires_auth('post:actors')
def add_actors(payload):
    body = request.get_json()
    new_name = body.get('name')
    new_age = body.get('age')
    new_gender = body.get('gender')
    if not (new_name and new_age and new_gender):
        abort(400)

    actor = Actor(
        name=new_name,
        age=new_age,
        gender=new_gender
    )
    try:
        actor.insert()
    except Exception as e:
        print(e)
        abort(422)

    current_actor = Actor.query.filter(and_(Actor.name == new_name, Actor.age == new_age, Actor.gender == new_gender)).order_by(Actor.id.desc()).first()
    if not current_actor:
        abort(422)

    return jsonify({
        'success': True,
        'actors': current_actor.details()
    })

# Add movie to db
@app.route('/movies', methods=['POST'])
@requires_auth('post:movies')
def add_movies(payload):
    body = request.get_json()
    new_title = body.get('title')
    new_release_date = body.get('release_date')
    if not (new_title and new_release_date):
        abort(400)

    movie = Movie(
        title=new_title,
        release_date=new_release_date
    )
    try:
        movie.insert()
    except Exception as e:
        print(e)
        abort(422)

    current_movie = Movie.query.filter(and_(Movie.title == new_title, Movie.release_date == new_release_date)).order_by(Movie .id.desc()).first()
    if not current_movie:
        abort(422)

    return jsonify({
        'success': True,
        'movies': current_movie.details()
    })

# Update actor attributes
@app.route('/actors/<int:actor_id>', methods=['PATCH'])
@requires_auth('patch:actors')
def update_actors(payload, actor_id):
    body = request.get_json()
    if not actor_id:
        abort(400)
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    if not actor:
        abort(422)

    if body.get('name'):
        actor.name = body.get('name')
    if body.get('age'):
        actor.age = body.get('age')
    if body.get('gender'):
        actor.gender = body.get('gender')
    
    try:
        actor.update()
    except Exception as e:
        print(e)
        abort(422)

    return jsonify({
        'success': True,
        'actors': actor.details()
    })

# Update movie attributes
@app.route('/movies/<int:movie_id>', methods=['PATCH'])
@requires_auth('patch:movies')
def update_movies(payload, movie_id):
    body = request.get_json()
    if not movie_id:
        abort(404)
    movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
    if not movie:
        abort(422)

    if body.get('title'):
        movie.title = body.get('title')
    if body.get('release_date'):
        movie.release_date = body.get('release_date')

    try:
        movie.update()
    except Exception as e:
        print(e)
        abort(422)

    return jsonify({
        'success': True,
        'movies': movie.details()
    })

# Delete actor from db
@app.route('/actors/<int:actor_id>', methods=['Delete'])
@requires_auth('delete:actors')
def delete_actors(payload, actor_id):
    if not actor_id:
        abort(404)
    actor = Actor.query.filter(Actor.id == actor_id).one_or_none()
    if not actor:
        abort(422)

    try:
        actor.delete()
    except Exception as e:
        print(e)
        abort(422)

    return jsonify({
        'success': True,
        'delete': actor.id
    })

# Delete movie from db
@app.route('/movies/<int:movie_id>', methods=['Delete'])
@requires_auth('delete:movies')
def delete_movies(payload, movie_id):
    if not movie_id:
        abort(404)
    movie = Movie.query.filter(Movie.id == movie_id).one_or_none()
    if not movie:
        abort(422)

    try:
        movie.delete()
    except Exception as e:
        print(e)
        abort(422)

    return jsonify({
        'success': True,
        'delete': movie.id
    })

# Error Handling
@app.errorhandler(422)
def unprocessable(error):
    return jsonify({
        "success": False,
        "error": 422,
        "message": "unprocessable"
    }), 422


@app.errorhandler(404)
def resource_not_found(error):
    return jsonify({
        "success": False,
        "error": 404,
        "message": "resource not found"
    }), 404


@app.errorhandler(AuthError)
def resource_not_found(error):
    return jsonify({
        "success": False,
        "error": 401,
        "message": "authentication error"
    }), 401

@app.errorhandler(400)
def resource_not_found(error):
    return jsonify({
        "success": False,
        "error": 400,
        "message": "bad request"
    }), 400
