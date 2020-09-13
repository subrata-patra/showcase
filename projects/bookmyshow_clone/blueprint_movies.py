from flask import Blueprint
from flask import Flask
from flask import request
import csv
import json
import jwt
import time

movies = Blueprint('movies', __name__)

@movies.route('/')
def movies_home():
    return "Welcome to *Movies* Home Page!"

### Create Movie Details:
@movies.route('/create', methods = ['POST'])
def movie_details_create():
    iid = request.json['iid']
    movie_name = request.json['movie_name']
    year = request.json['year']
    duration = request.json['duration']
    user_id = request.json['user_id']
    auth_token = request.json['auth_token']
    dict1 = {}
    dict1['iid'] = iid
    dict1['movie_name'] = movie_name
    dict1['year'] = year
    dict1['duration'] = duration
    dict1['user_id'] = user_id

    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data['expire'] >= time.time():
        with open('data/movies.csv', 'a') as file_wrap: 
            headers = dict1.keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writerow(dict1)        
        return json.dumps({'message':'bus details created'})
    else:
         return json.dumps({'message':'token invalid'})


### Get All Movie Details:
@movies.route('/details', methods = ['POST'])
def show_movie_details():
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data['expire'] >= time.time():
        with open('data/movies.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            csv_mlist = list(csv_obj)
        return json.dumps({'movies': csv_mlist}) 
    else:
        return json.dumps({'message':'token invalid'})

### Searh for a Movie using Novie Name:
@movies.route('/search', methods = ['POST'])
def movie_search():
    movie_name = request.json['movie_name']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['expire'] >= time.time():
        with open('data/movies.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            for odict in csv_obj:
                if odict['movie_name'] == movie_name: 
                    return json.dumps({'movie details': odict})
    else: 
        return json.dumps({'message':'token invalid'})
              
### Delete a Movie Details:
@movies.route('/delete', methods = ['DELETE'])
def movie_delete():
    movie_name = request.json['movie_name']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['expire'] >= time.time():
        with open('data/movies.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            main_list = []
            for i in csv_obj:
                main_list.append(i)
     
        with open('data/movies.csv', 'w') as file_wrap:
            headers = main_list[0].keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writeheader()
            for odict in main_list:
                if odict['movie_name'] != movie_name:
                    csv_template.writerow(odict)
        return json.dumps({'message': 'movie details deleted'})
    else:
        return json.dumps({'message':'token invalid'})
   

### Modity a Movie Details:
@movies.route('/modify_year', methods = ['PATCH'])
def movie_modify_year():
    movie_name = request.json['movie_name']
    year_mod = request.json['year_mod']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['expire'] >= time.time():
        with open('data/movies.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            main_list = []
            for odict in csv_obj:
                if odict['movie_name'] == movie_name:
                    odict['year'] = year_mod
                    main_list.append(odict)
                else:
                    main_list.append(odict)
                         
        with open('data/movies.csv', 'w') as file_wrap:
            headers = main_list[0].keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writeheader()
            for row in main_list:
                csv_template.writerow(row)
            
        return json.dumps({'message': 'movie year modified'})
    else:
        return json.dumps({'message':'invalid token'})
    