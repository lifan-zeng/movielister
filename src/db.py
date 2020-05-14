from flask_sqlalchemy import SQLAlchemy
import time

# To do:
# - Add creator and contributers field to list
# - Add friends to User -> be sure to cascade delete
# - Allow friend request accept/deny
# - View if friends have seen movie

db = SQLAlchemy()

#association table between User and WatchedList
user_movie_list_table = db.Table('user_movie_list', db.Model.metadata,
    db.Column('user_id', db.Integer, db.ForeignKey('user.id')),
    db.Column('movie_list_id', db.Integer, db.ForeignKey('movie_list.id'))  
)

#association table between MovieList and Movie
movie_in_list_table = db.Table('movie_in_list', db.Model.metadata,
    db.Column('movie_list_id', db.Integer, db.ForeignKey('movie_list.id')),
    db.Column('movie_id', db.Integer, db.ForeignKey('movie.id'))
)

#association table for friends in User
friend_table = db.Table('friend', db.Model.metadata,
    db.Column('user_id_1', db.Integer, db.ForeignKey('user.id')),
    db.Column('user_id_2', db.Integer, db.ForeignKey('user.id'))
)

class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, nullable=False)
    email = db.Column(db.String, nullable=False)
    time_created = db.Column(db.Integer, nullable=False)
    # movie_lists = db.relationship('MovieList', secondary=user_movie_list_table, back_populates='user', cascade='delete')
    movie_lists = db.relationship('MovieList', cascade='delete')
    friends = db.relationship('User',
                    secondary = friend_table,
                    primaryjoin = id==friend_table.c.user_id_1,
                    secondaryjoin = id==friend_table.c.user_id_2,
                    backref='user_id_2'
    )

    #add relationships

    def __init__(self, **kwargs):
        self.username = kwargs.get('username', '')
        self.email = kwargs.get('email', '')
        self.time_created = int(time.time())

    def serialize(self):
        return {
            'id': self.id,
            'username': self.username,
            'email': self.email,
            'time_created': self.time_created,
            'movie_lists': [ml.serialize() for ml in self.movie_lists]
        }


class MovieList(db.Model):
    __tablename__ = 'movie_list'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    # user = db.relationship('User', secondary=user_movie_list_table, back_populates='movie_lists')
    

    # watched_list = db.relationship('WatchedList', back_populates='movie_list', cascade='delete') 
    # plan_to_watch_list = db.relationship('PlanToWatchList', back_populates='movie_list', cascade='delete') 
    # play_list = db.relationship('PlayList', back_populates='movie_list', cascade='delete') 

    movies = db.relationship('Movie', secondary=movie_in_list_table, back_populates='lists')

    #add relationships

    # list_type = db.Column(db.String)
    # __mapper_args__ = {
    #     'polymorphic_identity':'list',
    #     'polymorphic_on': list_type
    # }

    def __init__(self, **kwargs):
        self.name = kwargs.get('name', '')
        self.user_id = kwargs.get('user_id', 1)

    def serialize(self, show_movies=True):
        serial = {
            'id': self.id,
            'name': self.name
        }
        if show_movies:
            serial['movies'] = [m.serialize() for m in self.movies]
        return serial


# class WatchedList(db.Model):
#     __tablename__ = 'watched_list'

#     id = db.Column(db.Integer, primary_key=True)
#     movie_list_id = db.Column(db.Integer, db.ForeignKey('movie_list.id'))
#     movie_list = db.relationship('User', uselist=False, back_populates='watched_list')

#     def __init__(self, **kwargs):
#         self.movie_list_id = kwargs.get('movie_list_id')
    
#     # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), back_populates='watched_list')
    
#     # def __init__(self, **kwargs):
#     #     super().__init__(self, **kwargs)

#     # __mapper_args__ = {
#     #     'polymorphic_identity':'watched movie list',
#     # }


# class PlanToWatchList(MovieList):
#     __tablename__ = 'plan_to_watch_list'

#     id = db.Column(db.Integer, primary_key=True)
#     movie_list_id = db.Column(db.Integer, db.ForeignKey('movie_list.id'))
#     movie_list = db.relationship('User', uselist=False, back_populates='plan_to_watch_list')
    
#     def __init__(self, **kwargs):
#         self.movie_list_id = kwargs.get('movie_list_id')

#     # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), back_populates='plan_to_watch_list')
    
#     # def __init__(self, **kwargs):
#     #     super().__init__(self, **kwargs)

#     # __mapper_args__ = {
#     #     'polymorphic_identity':'plan to watch movie list'
#     # }


# class PlayList(MovieList):
#     __tablename__ = 'play_list'

#     id = db.Column(db.Integer, primary_key=True)
#     movie_list_id = db.Column(db.Integer, db.ForeignKey('movie_list.id'))
#     movie_list = db.relationship('User', uselist=False, back_populates='play_list')

#     def __init__(self, **kwargs):
#         self.movie_list_id = kwargs.get('movie_list_id')

    
#     # user_id = db.Column(db.Integer, db.ForeignKey('user.id'), back_populates='play_list')

#     # def __init__(self, **kwargs):
#     #     super().__init__(self, **kwargs)

#     # __mapper_args__ = {
#     #     'polymorphic_identity':'play list'
#     # }


class Movie(db.Model):
    __tablename__ = 'movie'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    director = db.Column(db.String, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    lists = db.relationship('MovieList', secondary=movie_in_list_table, back_populates='movies')

    def __init__(self, **kwargs):
        self.title = kwargs.get('title', '')
        self.director = kwargs.get('director', '')
        self.year = kwargs.get('year', '')
    
    def serialize(self):
        return {
            'id': self.id,
            'title': self.title,
            'director': self.director,
            'year': self.year,
            'lists': [l.serialize(show_movies=False) for l in self.lists]
        }


