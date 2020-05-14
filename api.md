#API

This is the movielister API.

Public IP: http://35.197.39.103/

## `GET` `/api/users/`
### Description

gets all users

### Response

    {
      "success": true,
      "data": [
        {
          "id": 1,
          "username": "lifanzeng",
          "email": "lhz3@cornell.edu",
          "time_created": 1589460084, //unix time
          "movie_lists": [ (SERIALIZED MOVIE LIST), ... ],
          "friends": [ (SERIALIZED USER WITH ID AND USERNAME FIELDS ONLY), ... ]
        }
        ...
      ]
    }

## `GET` `/api/users/{id}/`
### Description

get specific user by id

### Response

    {
        "success": true,
        "data": {
            "id": (ID),
            "username": (USER INPUT FOR USERNAME),
            "email": (USER INPUT FOR EMAIL),
            "time_created": 1589465114,
            "movie_lists": [ (SERIALIZED MOVIE LIST), ... ],
            "friends": [ (SERIALIZED USER WITH ID AND USERNAME FIELDS ONLY), ... ]
        }
    }

## `POST` `/api/users/`
### Description

create user

### Request

    {
        "username": (USER INPUT)
        "email": (USER INPUT)
    }
    

### Response

    {
        "success": true,
        "data": {
            "id": (ID),
            "username": (USER INPUT),
            "email": (USER INPUT),
            "time_created": (TIME CREATED),
            "movie_lists": [
                {
                    "id": 1,
                    "name": "Watched",
                    "owner_id": 1,
                    "movies": []
                },
                {
                    "id": 2,
                    "name": "Plan to Watch",
                    "owner_id": 1,
                    "movies": []
                }
            ],
            "friends": []
        }
    }

## `DEL` `/api/users/{id}/`
### Description

deletes user by id

### Response

    {
        "success": true,
        "data": {
            "id": (ID),
            "username": (USER INPUT FOR USERNAME),
            "email": (USER INPUT FOR EMAIL),
            "time_created": 1589465114,
            "movie_lists": [ (SERIALIZED MOVIE LIST), ... ],
            "friends": [ (SERIALIZED USER WITH ID AND USERNAME FIELDS ONLY), ... ]
        }
    }

## `POST` `/api/users/{id}/`
### Description

updates user by id

### Request

    {
        "username": (USER INPUT FOR USERNAME, OPTIONAL),
        "email": (USER INPUT FOR EMAIL, OPTIONAL)
    }
    

### Response

    {
        "success": true,
        "data": {
            "id": (ID),
            "username": (USER INPUT FOR USERNAME),
            "email": (USER INPUT FOR EMAIL),
            "time_created": 1589465114,
            "movie_lists": [ (SERIALIZED MOVIE LIST), ... ],
            "friends": [ (SERIALIZED USER WITH ID AND USERNAME FIELDS ONLY), ... ]
        }
    }

## `POST` `/api/users/{id1}/friend/{id2}/`
### Description

adds user id1 and id2 as friends

### Response

    {
        "success": true,
        "data": {
            "id": (ID1),
            "username": (USER INPUT FOR USERNAME),
            "email": (USER INPUT FOR EMAIL),
            "time_created": 1589465114,
            "movie_lists": [ (SERIALIZED MOVIE LIST), ... ],
            "friends": [ (SERIALIZED USER WITH ID AND USERNAME FIELDS ONLY), ... ]
        }
    }

## `POST` `/api/users/{id1}/unfriend/{id2}/`
### Description

removes user id1 and id2 as friends

### Response

    {
        "success": true,
        "data": {
            "id": (ID1),
            "username": (USER INPUT FOR USERNAME),
            "email": (USER INPUT FOR EMAIL),
            "time_created": 1589465114,
            "movie_lists": [ (SERIALIZED MOVIE LIST), ... ],
            "friends": [ (SERIALIZED USER WITH ID AND USERNAME FIELDS ONLY), ... ]
        }
    }

## `GET` `/api/lists/`
### Description

gets all lists

### Response

    {
        "success": true,
        "data": [
            {
                "id": 1,
                "name": "Watched",
                "owner_id": 1,
                "movies": [ (MOVIE SERIALIZED), ... ]
            },
            {
                "id": 2,
                "name": "Plan to Watch",
                "owner_id": 1,
                "movies": [ (MOVIE SERIALIZED), ... ]
            }
        ]
        ...
    }

## `GET` `/api/lists/{id}/'
### Description

gets list by id

### Response

    {
        "success": true,
        "data": {
            "id": (ID),
            "name": (USER INPUT FOR NAME),
            "owner_id": (USER ID),
            "movies": [ (MOVIE SERIALIZED), ... ]
        }
    }

## `POST` `/api/users/{id}/list/`
### Description

creates a list for user id

### Request

    {
    	"name": (USER INPUT)
    }
    

### Response

    {
        "success": true,
        "data": {
            "id": (ID),
            "name": (USER INPUT FOR LIST NAME),
            "owner_id": (USER ID),
            "movies": []
        }
    }

## `POST` `/api/lists/{id}/`
### Description

updates a list for user id

### Request

    {
    	"name": (USER INPUT, OPTIONAL),
    	"add_movies": [ (USER INPUT FOR MOVIE ID, OPTIONAL), ... ],
    	"remove_movies": [ (USER INPUT FOR MOVIE ID, OPTIONAL), ... ]
    }
    

### Response

    {
        "success": true,
        "data": {
            "id": (ID),
            "name": (USER INPUT FOR LIST NAME),
            "owner_id": (USER ID),
            "movies": [ (MOVIE SERIALIZED), ... ]
        }
    }

## `DEL` `/api/lists/{id}`
### Description

deletes list of list id

### Response

     {
        "success": true,
        "data": {
            "id": (ID),
            "name": (USER INPUT FOR LIST),
            "owner_id": (USER ID),
            "movies": [ (MOVIE SERIALIZED) ... ]
        }
    }

## `GET` `/api/movies/`
### Description

gets all movies

### Response

    {
        "success": true,
        "data": [
            {
                "id": 1,
                "title": "Zombieland",
                "director": "Ruben Fleischer",
                "year": 2009,
                "lists": [  (SERIALIZED LIST WITHOUT MOVIES FIELD), ... ]
            }
            ...
        ]
    }

## `GET` `/api/movies/{id}`
### Description

gets movie by movie id

### Response

    {
        "success": true,
        "data": {
            "id": (ID),
            "title": (USER INPUT FOR TITLE),
            "director": (USER INPUT FOR DIRECTOR),
            "year": (USER INPUT FOR YEAR),
            "lists": [ (SERIALIZED LIST WITHOUT MOVIES FIELD), ... ]
        }
    }

## `POST` `/api/movies/`
### Description

adds a movie

### Request

    {
    	"title": (USER INPUT FOR MOVIE TITLE),
    	"director": (USER INPUT FOR DIRECTOR),
    	"year": (USER INPUT FOR YEAR)
    }
    

### Response

    {
        "success": true,
        "data": {
            "id": (ID),
            "title": (USER INPUT FOR MOVIE TITLE),
            "director": (USER INPUT FOR MOVIE DIRECTOR),
            "year": (USER INPUT FOR MOVIE YEAR),
            "lists": []
        }
    }

## `POST` `/api/users/{id}`
### Description

updates movie by id

### Request

    {
    	"title": (USER INPUT FOR MOVIE TITLE, OPTIONAL),
    	"director": (USER INPUT FOR DIRECTOR, OPTIONAL),
    	"year": (USER INPUT FOR YEAR, OPTIONAL)
    }
    

### Response

    {
        "success": true,
        "data": {
            "id": (ID),
            "title": (USER INPUT FOR MOVIE TITLE),
            "director": (USER INPUT FOR MOVIE DIRECTOR),
            "year": (USER INPUT FOR MOVIE YEAR),
            "lists": []
        }
    }

## `DEL` `/api/users/{id}`
### Description

deletes a movie by id

### Response

    {
            "id": (ID),
            "title": (USER INPUT FOR MOVIE TITLE),
            "director": (USER INPUT FOR MOVIE DIRECTOR),
            "year": (USER INPUT FOR MOVIE YEAR),
            "lists": []
        }

