from db import db, User, MovieList, Movie
from sqlalchemy.orm import with_polymorphic

def get_all_users():
    return [u.serialize() for u in User.query.all()]

def create_user(username, email):
    new_user = User(username=username,email=email)
    db.session.add(new_user)
    db.session.commit()
    new_watched_list = create_movie_list(name='Watched', user_id=new_user.id)
    new_plan_to_watch_list = create_movie_list(name='Plan to Watch', user_id=new_user.id)
    # _create_default_lists(new_user.id)
    return new_user.serialize()

def _create_default_lists(user_id):
    print('entered default')
    user = get_user_by_id(user_id)
    if user is None:
        return None
    new_watched_list = create_movie_list(name='Watched', user_id=user_id)
    new_plan_to_watch_list = create_movie_list(name='Plan to Watch', user_id=user_id)

def get_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    return user.serialize()

def update_user_by_id(user_id, body):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    
    user.username = body.get('username', user.username)
    user.email = body.get('email', user.email)
    db.session.commit()
    return user.serialize()

def delete_user_by_id(user_id):
    user = User.query.filter_by(id=user_id).first()
    if user is None:
        return None
    db.session.delete(user)
    db.session.commit()
    return user.serialize()

def add_user_as_friend(user_id_1, user_id_2):
    user_1 = get_user_by_id(user_id_1)
    user_2 = get_user_by_id(user_id_2)
    if (user_1 or user_2) is None:
        return None
    user_1.friends.append(user_2)
    user_2.friends.append(user_1)
    return user_1.serialize()
    

def create_movie_list(name, user_id):
    new_list = MovieList(name=name, user_id=user_id)
    user = get_user_by_id(user_id)
    if user is None:
        return None
    db.session.add(new_list)
    db.session.commit()
    return new_list.serialize()

def get_all_lists():
    return [l.serialize() for l in MovieList.query.all()]

def get_all_movies():
    return [u.serialize() for u in Movie.query.all()]

def get_movie_list_by_id(movie_list_id):
    movie_list = MovieList.query.filter_by(id=movie_list_id).first()
    if movie_list is None:
        return None
    return movie_list.serialize()

def update_movie_list_by_id(movie_list_id, body):
    movie_list = MovieList.query.filter_by(id=movie_list_id).first()
    if movie_list is None:
        return None
    movie_list.name = body.get('name', movie_list.name)
    movies_to_add = body.get('movies', None)
    movies_not_added = []
    if movies_to_add is not None:
        for movie_id in movies_to_add:
            movie = get_movie_by_id(movie_id)
            if movie is None:
                movies_not_added.append(movie_id)
            movie_list.movies.append(list(movie))
    db.session.commit()
    return movie_list.serialize()
            
    #ADD THE "ADD MOVIE" OPTION    

    

def delete_movie_list_by_id(movie_list_id):
    movie_list = MovieList.query.filter_by(id=movie_list_id).first()
    if movie_list is None:
        return None
    db.session.delete(movie_list)
    db.session.commit()
    return movie_list.serialize()
 
def add_movie(title, director, year):
    new_movie = Movie(title=title, director=director, year=year)
    db.session.add(new_movie)
    db.session.commit()
    return new_movie.serialize()

def get_movie_by_id(movie_id):
    movie = MovieList.query.filter_by(id=movie_id).first()
    if movie is None:
        return None
    return movie.serialize()

def update_movie_by_id(movie_id, body):
    movie = MovieList.query.filter_by(id=movie_id).first()
    if movie is None:
        return None
    movie.title = body.get('title', movie.title)
    movie.director = body.get('director', movie.director)
    movie.year = body.get('year', movie.year)
    db.session.commit()
    return movie.serialize()

def delete_movie_by_id(movie_id):
    movie = MovieList.query.filter_by(id=movie_id).first()
    if movie is None:
        return None
    db.session.delete(movie)
    db.session.commit()
    return movie.serialize()
