from flask import Blueprint
from flask import Flask
from flask import request
import csv
import json
import jwt
import time

comments = Blueprint('comments', __name__)

@comments.route('/')
def comments_home():
    return "Welcome to *Comments* Home Page!"

### Create Comment Details:
@comments.route('/create', methods = ['POST'])
def comment_details_create():
    iid = request.json['iid']
    comment = request.json['comment']
    movie_id = request.json['movie_id']
    user_id = request.json['user_id']
    auth_token = request.json['auth_token']
    dict1 = {}
    dict1['iid'] = iid
    dict1['comment'] = comment
    dict1['movie_id'] = movie_id
    dict1['user_id'] = user_id

    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data['expire'] >= time.time():
        with open('data/comments.csv', 'a') as file_wrap: 
            headers = dict1.keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writerow(dict1)        
        return json.dumps({'message':'comment created'})
    else:
         return json.dumps({'message':'token invalid'})


### Get All Comment Details:
@comments.route('/details', methods = ['POST'])
def show_comment_details():
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)
    if data['expire'] >= time.time():
        with open('data/comments.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            csv_mlist = list(csv_obj)
        return json.dumps({'comments': csv_mlist}) 
    else:
        return json.dumps({'message':'token invalid'})

### Searh for a Comment by Movie ID:
@comments.route('/search', methods = ['POST'])
def comment_search():
    movie_id = request.json['movie_id']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['expire'] >= time.time():
        with open('data/comments.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            for odict in csv_obj:
                if odict['movie_id'] == movie_id: 
                    return json.dumps({'comment details': odict})
    else: 
        return json.dumps({'message':'token invalid'})
              
### Delete a Comment Details:
@comments.route('/delete', methods = ['DELETE'])
def comment_delete():
    movie_id = request.json['movie_id']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['expire'] >= time.time():
        with open('data/comments.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            main_list = []
            for i in csv_obj:
                main_list.append(i)
     
        with open('data/comments.csv', 'w') as file_wrap:
            headers = main_list[0].keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writeheader()
            for odict in main_list:
                if odict['movie_id'] != movie_id:
                    csv_template.writerow(odict)
        return json.dumps({'message': 'comment details deleted'})
    else:
        return json.dumps({'message':'token invalid'})
   

### Modity a Comment Details:
@comments.route('/modify_comment', methods = ['PATCH'])
def commnet_modify():
    movie_id = request.json['movie_id']
    comment_mod = request.json['comment_mod']
    auth_token = request.json['auth_token']
    key = 'secret'
    data = jwt.decode(auth_token, key)

    if data['expire'] >= time.time():
        with open('data/comments.csv', 'r') as file_wrap:
            csv_obj = csv.DictReader(file_wrap)
            main_list = []
            for odict in csv_obj:
                if odict['movie_id'] == movie_id:
                    odict['comment'] = comment_mod
                    main_list.append(odict)
                else:
                    main_list.append(odict)
                         
        with open('data/comments.csv', 'w') as file_wrap:
            headers = main_list[0].keys()
            csv_template = csv.DictWriter(file_wrap, fieldnames = headers)
            csv_template.writeheader()
            for row in main_list:
                csv_template.writerow(row)
            
        return json.dumps({'message': 'comment modified'})
    else:
        return json.dumps({'message':'invalid token'})
    