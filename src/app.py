from flask import Flask, request
from db import db
import json
import dao

app = Flask(__name__)
db_filename = 'movie_lister.db'

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///%s" % db_filename
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_ECHO"] = True

db.init_app(app)
with app.app_context():
    db.create_all()

def success_response(data, code=200): 
    return json.dumps({"success": True, "data": data}), code

def failure_response(message, code=404):
    return json.dumps({"success": False, "error": message}), code

@app.route('/api/users/')
def get_users():
    return success_response(dao.get_all_users())

@app.route('/api/users/<int:user_id>/')
def get_user(user_id):
    user = dao.get_user_by_id(user_id)
    if user is None:
        return failure_response('User not found')
    return success_response(user)

@app.route('/api/users/', methods=['POST'])
def create_user():
    body = json.loads(request.data)
    user = dao.create_user(
        username=body.get('username'),
        email=body.get('email')
    )
    return success_response(user, 201)

@app.route('/api/users/<int:user_id>/', methods=['DELETE'])
def delete_user(user_id):
    user = dao.delete_user_by_id(user_id)
    if user is None:
        return failure_response('User not found')
    return success_response(user)

@app.route('/api/users/<int:user_id>/', methods=['POST'])
def update_user(user_id):
    body = json.loads(request.data)
    user = dao.update_user_by_id(
        user_id,
        body
    )
    if user is None:
        return failure_response('User not found')
    return success_response(user)

@app.route('/api/users/<int:user_id_1>/friend/<int:user_id_2>/', methods=['POST'])
def add_friend(user_id_1, user_id_2):
    add = dao.add_user_as_friend(user_id_1, user_id_2)
    if add is None:
        return failure_response('User(s) not found')
    return success_response(add)

@app.route('/api/users/<int:user_id_1>/unfriend/<int:user_id_2>/', methods=['POST'])
def remove_friend(user_id_1, user_id_2):
    add = dao.remove_user_as_friend(user_id_1, user_id_2)
    if add is None:
        return failure_response('Error occurred in removing friend')
    return success_response(add)

@app.route('/api/lists/')
def get_lists():
    return success_response(dao.get_all_lists())

@app.route('/api/users/<int:user_id>/list/', methods=['POST'])
def create_list(user_id):
    body = json.loads(request.data)
    user = dao.get_user_by_id(user_id)
    movie_list = dao.create_movie_list(
        name=body.get('name'),
        user_id=user_id
    )
    return success_response(movie_list, 201)

@app.route('/api/lists/<int:list_id>/')
def get_list(list_id):
    movie_list = dao.get_movie_by_id(list_id)
    if movie_list is None:
        return failure_response('List not found')
    return success_response(movie_list)

@app.route('/api/lists/<int:list_id>/', methods=['POST'])
def update_list(list_id):
    body = json.loads(request.data)
    movie_list = dao.update_movie_list_by_id(list_id, body)
    if movie_list is None:
        return failure_response('Error occured in updating list')
    return success_response(movie_list)

@app.route('/api/lists/<int:list_id>/', methods=['DELETE'])
def delete_list(list_id):
    movie_list = dao.delete_movie_list_by_id(list_id)
    if movie_list is None:
        return failure_response('List not found')
    return success_response(movie_list)

@app.route('/api/movies/')
def get_movies():
    return success_response(dao.get_all_movies())

@app.route('/api/movies/<int:movie_id>/')
def get_movie(movie_id):
    movie = dao.get_movie_by_id(movie_id)
    if movie is None:
        return failure_response
    return success_response(movie)

@app.route('/api/movies/', methods=['POST'])
def add_movie():
    body = json.loads(request.data)
    movie = dao.add_movie(
        title=body.get('title'),
        director=body.get('director'),
        year=body.get('year')
    )
    if movie is None:
        return failure_response('Movie not found')
    return success_response(movie)

@app.route('/api/movies/<int:movie_id>/', methods=['POST'])
def update_movie(movie_id):
    body = json.loads(request.data)
    movie = dao.update_movie_by_id(movie_id, body)
    if movie is None:
        return failure_response('Movie not found')
    return success_response(movie)

@app.route('/api/movies/<int:movie_id>/', methods=['DELETE'])
def delete_movie(movie_id):
    movie = dao.delete_movie_by_id(movie_id)
    if movie is None:
        return failure_response('Movie not found')
    return success_response(movie)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)